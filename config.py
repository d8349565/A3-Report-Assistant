# =============================================================
# A3 Report Assistant Configuration
# =============================================================

# -------------------------------------------------------------
# API Configuration
# -------------------------------------------------------------
DEEPSEEK_API_KEY = "sk-1f7fb773d0e94e2f8bf55ef2ff0c188c"  # 启动时自动检查并提示输入
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"

# -------------------------------------------------------------
# Application Configuration
# -------------------------------------------------------------
APP_SECRET_KEY = "A3-Assistant-Secret"
OUTPUT_DIR_NAME = "output"
ADMIN_PASSWORD = "admin123"  # 管理员密码，建议在生产环境中修改

# -------------------------------------------------------------
# Document Configuration
# -------------------------------------------------------------
DOC_FONT_NAME = "宋体"
DOC_TITLE_TEMPLATE = "A3 报告优化 – {topic}"

# -------------------------------------------------------------
# AI Prompt Templates
# -------------------------------------------------------------
SYSTEM_PROMPTS = {
    "default": "你是一名精通 A3方法的精益顾问，用简洁中文回复，注意段落换行。",
    "step_guidance": """你是一名精通A3方法的精益顾问，你需要严格按照A3报告每一步的目的、工具和要点进行指导。

    当前步骤：{title}

    目的：{purpose}

    工具：{tools}

    要点：{focus}

    请用简洁中文回复。""",
    "validation": """以下是某 A3 报告已填写内容（可能不完整）：

    {context}

    请作为精益顾问，判断《{title}》段落是否符合该步骤的目的、工具及逻辑要求，若不充分，指出缺口并给出改进建议，总字数尽可能少。""",
    "optimization": "请在不改变原意的情况下，优化下面这段《{title}》文本，使其更符合 A3 报告规范，输出 200 字以内改进建议：\n{content}"
}

# -------------------------------------------------------------
# A3 Steps Guide
# -------------------------------------------------------------
GUIDE = [
    {
        "id": "step1",
        "title": "课题选择 / Select Topic",
        "purpose": "明确课题及方向",
        "tools": "可以参考使用矩阵数据分析表",
        "focus": "名词主体尽量1个，命名要使用动词+修饰词+名词结构；比如降低/提升/减少…",
    },
    {
        "id": "step2",
        "title": "明确问题 / Clarify Problem",
        "purpose": "梳理必要性、范围、定义",
        "tools": "推荐使用5W2H, 帕累托图, 分层法等方法",
        "focus": "数据 & 评估预期收益;（如果不能量化，可描述为可成为行业标杆之类）",
    },
    {
        "id": "step3",
        "title": "现状分析 / Current Situation",
        "purpose": "聚焦主要问题，把控当前状态",
        "tools": "5W2H, 帕累托图, 分层法",
        "focus": "2/8 原则；来源可靠; Y→Y1,Y2…",
    },
    {
        "id": "step4",
        "title": "设定目标 / Set Targets",
        "purpose": "方向 & 衡量",
        "tools": "柱状图, 趋势图",
        "focus": "基线值, 目标值, SMART",
    },
    {
        "id": "step5",
        "title": "原因分析 / Root Cause",
        "purpose": "寻找真因",
        "tools": "鱼骨图, 5Why, FMEA, 头脑风暴, IE",
        "focus": "选对工具, 逻辑闭环, 验证",
    },
    {
        "id": "step6",
        "title": "制定对策 / Countermeasures",
        "purpose": "提出针对性措施",
        "tools": "对策矩阵, 影响‑实施难度评估",
        "focus": "消除真因; 节点 / 责任 / 资源",
    },
    {
        "id": "step7",
        "title": "贯彻实施 / Implementation",
        "purpose": "行动落地",
        "tools": "甘特图, 责任分配表",
        "focus": "时间、责任人、检查点",
    },
    {
        "id": "step8",
        "title": "验证巩固 / Verify & Standardise",
        "purpose": "评估效果并防止回潮",
        "tools": "控制图, 审核清单",
        "focus": "前后对比 & SOP 更新",
    },
]

# -------------------------------------------------------------
# Model Options - 支持的模型列表
# -------------------------------------------------------------
SUPPORTED_MODELS = {
    "deepseek-chat": {
        "name": "deepseek-chat",
        "display_name": "标准模式",
        "description": "DeepSeek 标准聊天模型，适合日常对话和内容生成"
    },
    "deepseek-reasoner": {
        "name": "deepseek-reasoner", 
        "display_name": "思考模式",
        "description": "DeepSeek 推理模型，具备更强的逻辑推理和深度思考能力"
    }
} 