"""
A3 Report Assistant – Word Edition v0.3.1
========================================
* 输出 Word(docx)，兼容 DeepSeek API，保留 AI 检查功能。
* 依赖：flask python-docx openai
"""

from __future__ import annotations
import datetime as _dt
import json
import re
import sys
import os
import webbrowser
from pathlib import Path
from typing import Dict, List

from flask import (
    Flask,
    request,
    render_template_string,
    send_file,
    redirect,
    url_for,
    flash,
    jsonify,
)
import openai
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn

import config

def ensure_api_key():
    """检查API Key是否存在，Docker环境下跳过交互式输入"""
    api_key = os.getenv("DEEPSEEK_API_KEY") or getattr(config, "DEEPSEEK_API_KEY", None)
    if not api_key or not api_key.strip():
        # 在Docker环境中，如果没有API Key则退出
        if os.getenv("FLASK_ENV") == "production":
            print("错误: 未设置 DEEPSEEK_API_KEY 环境变量")
            print("请在 .env 文件中设置 DEEPSEEK_API_KEY")
            sys.exit(1)
        else:
            # 开发环境下保持原有交互式输入
            key = input("请输入 DeepSeek API Key：").strip()
            # 写入 config.py
            with open("config.py", "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open("config.py", "w", encoding="utf-8") as f:
                for line in lines:
                    if line.strip().startswith("DEEPSEEK_API_KEY"):
                        f.write(f'DEEPSEEK_API_KEY = "{key}"\n')
                    else:
                        f.write(line)
            print("API Key 已保存，请重新启动程序。")
            sys.exit(0)

# -------------------------------------------------------------
# Configuration
# -------------------------------------------------------------
OUTPUT_DIR = Path(__file__).parent / config.OUTPUT_DIR_NAME
OUTPUT_DIR.mkdir(exist_ok=True)

# 从config导入配置
GUIDE: List[Dict[str, str]] = config.GUIDE
# 优先从环境变量读取 API Key，用于Docker部署
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY") or config.DEEPSEEK_API_KEY

GUIDE_MAP = {g["id"]: g for g in GUIDE}

app = Flask(__name__)
app.secret_key = config.APP_SECRET_KEY

# -------------------------------------------------------------
# Helper functions
# -------------------------------------------------------------

def sanitize_filename(text: str) -> str:
    return re.sub(r"[^\w\- ]", "", text).strip()[:40] or "A3Report"


def next_docx_path(topic: str) -> Path:
    base = f"{_dt.datetime.now():%Y%m%d_%H%M}_{sanitize_filename(topic)}"
    idx = 1
    while True:
        p = OUTPUT_DIR / f"{base}_v{idx}.docx"
        if not p.exists():
            return p
        idx += 1


def call_deepseek(prompt: str, api_key: str = None, step_id: str = None) -> str:
    api_key = api_key or DEEPSEEK_API_KEY
    # 如果有step_id，拼接system prompt
    if step_id and step_id in GUIDE_MAP:
        st = GUIDE_MAP[step_id]
        sys_prompt = config.SYSTEM_PROMPTS["step_guidance"].format(
            title=st['title'],
            purpose=st['purpose'],
            tools=st['tools'],
            focus=st['focus']
        )
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt},
        ]
        return call_deepseek_multi(messages, api_key)
    # 否则用默认system prompt
    client = openai.OpenAI(api_key=api_key, base_url=config.DEEPSEEK_BASE_URL)
    try:
        resp = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=[
                {"role": "system", "content": config.SYSTEM_PROMPTS["default"]},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        return resp.choices[0].message.content.strip()
    except Exception as exc:
        return f"<LLM 调用失败> {exc}"


def build_doc(topic: str, user_inputs: Dict[str, str], suggestions: Dict[str, str]) -> Path:
    doc = Document()
    h = doc.add_heading(config.DOC_TITLE_TEMPLATE.format(topic=topic), level=1)
    h.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    for run in h.runs:
        set_font_simsun(run)

    for idx, st in enumerate(GUIDE, 1):
        heading = doc.add_heading(f"Step {idx}: {st['title']}", level=2)
        for run in heading.runs:
            set_font_simsun(run)
        p1 = doc.add_paragraph(user_inputs.get(st["id"], "(用户未填写)"))
        for run in p1.runs:
            set_font_simsun(run)
        p2 = doc.add_paragraph("优化建议：", style="Intense Quote")
        for run in p2.runs:
            set_font_simsun(run)
        p3 = doc.add_paragraph(suggestions.get(st["id"], "-"))
        for run in p3.runs:
            set_font_simsun(run)

    path = next_docx_path(topic)
    doc.save(path)
    return path

# -------------------------------------------------------------
# Web templates
# -------------------------------------------------------------

# 从config导入HTML模板
HTML = config.HTML_TEMPLATE

# -------------------------------------------------------------
# Routes
# -------------------------------------------------------------

@app.route("/")
def index():
    step_ids_json = json.dumps([g["id"] for g in GUIDE])
    return render_template_string(HTML, guide=GUIDE, step_ids=step_ids_json)


@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json(force=True)
    step_id = data.get("step_id")
    inputs = data.get("inputs", {})
    history = data.get("history", [])  # 新增：历史对话
    if step_id not in GUIDE_MAP:
        return jsonify({"error": "参数错误"}), 400

    context = "\n".join([f"{GUIDE_MAP[k]['title']}: {v}" for k, v in inputs.items() if v.strip()])
    # 拼接当前步骤的A3指导信息
    st = GUIDE_MAP[step_id]
    sys_prompt = config.SYSTEM_PROMPTS["step_guidance"].format(
        title=st['title'],
        purpose=st['purpose'],
        tools=st['tools'],
        focus=st['focus']
    )
    user_prompt = config.SYSTEM_PROMPTS["validation"].format(
        context=context,
        title=st['title']
    )
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    for msg in history:
        if msg.get("role") in ("user","assistant") and msg.get("content"):
            messages.append({"role": msg["role"], "content": msg["content"]})
    suggestion = call_deepseek_multi(messages)
    return jsonify({"suggestion": suggestion})


@app.route("/generate", methods=["POST"])
def generate():
    user_inputs = {g["id"]: request.form.get(g["id"], "").strip() for g in GUIDE}
    topic = user_inputs.get("step1", "A3_Topic")[:30]

    suggestions: Dict[str, str] = {}
    for st in GUIDE:
        content = user_inputs.get(st["id"], "")
        if not content:
            suggestions[st["id"]] = "(用户未填写)"
            continue
        prompt = config.SYSTEM_PROMPTS["optimization"].format(
            title=st['title'],
            content=content
        )
        suggestions[st["id"]] = call_deepseek(prompt, step_id=st["id"])

    path = build_doc(topic, user_inputs, suggestions)
    return send_file(path, as_attachment=True)

# -------------------------------------------------------------
# 新增多轮对话支持

def call_deepseek_multi(messages, api_key: str = None) -> str:
    api_key = api_key or DEEPSEEK_API_KEY
    client = openai.OpenAI(api_key=api_key, base_url=config.DEEPSEEK_BASE_URL)
    try:
        resp = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=messages,
            stream=False,
        )
        return resp.choices[0].message.content.strip()
    except Exception as exc:
        return f"<LLM 调用失败> {exc}"

def set_font_simsun(run):
    run.font.name = config.DOC_FONT_NAME
    run._element.rPr.rFonts.set(qn('w:eastAsia'), config.DOC_FONT_NAME)

# -------------------------------------------------------------
if __name__ == "__main__":
    ensure_api_key()
    webbrowser.open("http://localhost:3333")
    if getattr(sys, "frozen", False):
        from waitress import serve
        serve(app, host="0.0.0.0", port=3333)
    else:
        app.run(host="0.0.0.0", port=3333, debug=False)
