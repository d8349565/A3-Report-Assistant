# A3 报告助手 / A3 Report Assistant

> 基于 DeepSeek AI 的智能 A3 精益改进报告生成工具
> AI-Powered A3 Lean Improvement Report Generator

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/a3-report-assistant)
[![Python](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

---

## 📋 项目简介

A3 报告助手是一款基于 DeepSeek AI 的智能工具，帮助企业和个人快速生成符合精益管理标准的 A3 改进报告。通过 AI 辅助，它能够：

- ✅ **智能验证**：实时检查每个步骤的内容是否符合 A3 方法论
- ✅ **优化建议**：自动生成改进建议，提升报告质量
- ✅ **多轮对话**：支持与 AI 持续交流，完善报告内容
- ✅ **一键生成**：自动生成格式规范的 Word 文档
- ✅ **权限管理**：支持访问密码和管理员配置控制1

---

## 🚀 快速开始

### ⚡ 快速配置检查清单

在开始之前，请确保完成以下配置：

- [ ] 复制 `.env.example` 为 `.env`
- [ ] 在 `.env` 中填入 DeepSeek API Key
- [ ] 修改默认密码（访问密码 `WEB_ACCESS_PASSWORD` 和 管理员密码 `ADMIN_PASSWORD`）
- [ ] 修改 Flask 密钥（`APP_SECRET_KEY`）
- [ ] 确认端口配置（默认 9998）

### 方式一：Docker 部署（推荐）

**适合：快速部署、生产环境使用**

#### 1. 前置条件

- 安装 [Docker](https://www.docker.com/) 和 [Docker Compose](https://docs.docker.com/compose/)
- 准备 DeepSeek API Key（在 [DeepSeek 官网](https://platform.deepseek.com/) 注册获取）

#### 2. 配置环境变量

在项目根目录复制 `.env.example` 为 `.env` 并填入配置：

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的配置
# Windows 用户可以用记事本打开编辑
```

`.env` 文件内容示例：

```bash
# DeepSeek API 配置（必填）
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
DEEPSEEK_BASE_URL=https://api.deepseek.com
MODEL_NAME=deepseek-chat

# 安全配置（建议修改）
APP_SECRET_KEY=your-random-secret-key-here
WEB_ACCESS_PASSWORD=your_access_password
ADMIN_PASSWORD=your_admin_password

# 应用配置（可选）
PORT=9998
HOST=0.0.0.0
OUTPUT_DIR_NAME=output
DOC_FONT_NAME=宋体
```

#### 3. 启动服务

```bash
# 构建并启动容器
docker-compose up -d

# 查看运行状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

#### 4. 访问应用

打开浏览器访问：**http://localhost:9998**

默认访问密码：`123456`（可在 `config.py` 中修改）

#### 5. 停止服务

```bash
# 停止容器
docker-compose down

# 停止并删除数据卷
docker-compose down -v
```

---

### 方式二：本地运行

**适合：开发调试、本地使用**

#### 1. 前置条件

- Python 3.11 或更高版本
- pip 包管理器

#### 2. 安装依赖

```bash
# 克隆或下载项目
cd A3报告助手

# 安装 Python 依赖
pip install -r requirements.txt
```

#### 3. 配置应用

**方式一：使用 .env 文件（推荐）**

复制环境变量模板并编辑：

```bash
# 复制模板
cp .env.example .env

# 编辑 .env 文件，至少填入以下必填项：
# DEEPSEEK_API_KEY=your_api_key_here
```

**方式二：直接编辑 config.py**

编辑 `config.py` 文件，填入你的 DeepSeek API Key：

```python
DEEPSEEK_API_KEY = "your_api_key_here"
```

首次运行时如未配置，程序会提示输入并自动保存。

#### 4. 启动应用

```bash
python A3.py
```

应用会自动打开浏览器并访问 **http://localhost:9998**

---

## 📖 使用指南

### 1. 登录系统

首次访问需要输入访问密码（默认：`123456`）

![登录页面示意](https://via.placeholder.com/600x300?text=Access+Login+Page)

### 2. 填写 A3 报告

按照 8 个步骤填写报告内容：

| 步骤   | 名称     | 说明                   |
| ------ | -------- | ---------------------- |
| Step 1 | 课题选择 | 明确改进课题和方向     |
| Step 2 | 明确问题 | 定义问题范围和必要性   |
| Step 3 | 现状分析 | 分析当前状态和主要问题 |
| Step 4 | 设定目标 | 制定可衡量的改进目标   |
| Step 5 | 原因分析 | 深入分析问题根本原因   |
| Step 6 | 制定对策 | 提出针对性的解决方案   |
| Step 7 | 贯彻实施 | 制定行动计划并执行     |
| Step 8 | 验证巩固 | 评估效果并标准化       |

### 3. 实时验证

点击任意步骤的"验证"按钮，AI 会：

- 检查内容是否符合该步骤的要求
- 指出不足之处
- 提供改进建议

![验证功能示意](https://via.placeholder.com/600x300?text=Real-time+Validation)

### 4. 多轮对话

在验证对话框中可以继续提问，AI 会基于上下文回答：

- "如何使用鱼骨图分析原因？"
- "这个目标是否符合 SMART 原则？"
- "能给出具体的对策示例吗？"

### 5. 生成报告

完成所有步骤后，点击"生成 A3 报告"：

- 自动生成 Word 文档（.docx 格式）
- 包含用户填写的内容和 AI 优化建议
- 文件保存在 `output` 目录

---

## ⚙️ 管理员配置

访问 `/admin` 路径进入管理后台（默认密码：`admin123`）

### 配置存储说明

配置项分为两类：

#### 1. 环境配置（保存到 `.env` 文件）

- **API 设置**：DeepSeek API Key、Base URL、模型名称
- **文档配置**：字体、标题模板
- **密码配置**：网页访问密码

这些配置修改后会立即保存到 `.env` 文件并生效。

#### 2. 业务配置（保存到 `config.py` 文件）

- **系统提示词**：AI 的指导风格和专业度
- **A3 步骤定义**：每个步骤的标题、目的、工具、要点

这些配置修改后保存到 `config.py` 文件，应用会自动重新加载。

**注意：** 在管理后台修改的配置会实时生效，无需重启应用。

---

## 📁 项目结构

```
A3报告助手/
├── A3.py                  # 主程序文件
├── config.py              # 配置文件（从环境变量读取）
├── .env.example           # 环境变量模板
├── .env                   # 环境变量配置（不提交到 Git）
├── .gitignore             # Git 忽略文件配置
├── requirements.txt       # Python 依赖
├── Dockerfile             # Docker 镜像配置
├── docker-compose.yml     # Docker Compose 配置
├── README.md              # 项目说明文档
├── templates/             # HTML 模板目录
│   ├── index.html         # 主页面
│   ├── access_login.html  # 访问登录页
│   ├── admin_login.html   # 管理员登录页
│   └── admin.html         # 管理后台页面
└── output/                # 生成的报告文件目录
```

---

## 🔐 安全建议

### 1. 使用 .env 文件管理敏感信息

**推荐做法：**

```bash
# 1. 复制环境变量模板
cp .env.example .env

# 2. 编辑 .env 文件，填入真实配置
# 3. 确保 .env 文件已添加到 .gitignore（已默认配置）
```

**重要提示：**

- ⚠️ **不要将 `.env` 文件提交到 Git 仓库**
- ⚠️ **不要在代码中硬编码 API Key 和密码**
- ✅ 使用 `.env.example` 作为配置模板供他人参考

### 2. 修改默认密码

在 `.env` 文件中修改以下配置：

```bash
# 网页访问密码（用户登录前台）
WEB_ACCESS_PASSWORD=your_strong_password

# 管理员密码（访问后台配置）
ADMIN_PASSWORD=your_admin_password

# Flask 密钥（用于 session 加密）
APP_SECRET_KEY=your_random_secret_key_here
```

生成强密钥的方法：

```bash
# Python 生成随机密钥
python -c "import secrets; print(secrets.token_hex(32))"
```

### 3. 保护 API Key

- ✅ Docker 部署时通过 `.env` 文件传递
- ✅ 本地开发时使用 `.env` 文件
- ✅ 生产环境使用环境变量或密钥管理服务
- ❌ 不要在 `config.py` 中硬编码真实的 API Key

### 4. 生产环境部署

- 使用 HTTPS 加密传输
- 配置防火墙规则
- 定期备份 `output` 目录

---

## 🛠️ 技术栈

- **后端框架**：Flask 2.3+
- **AI 模型**：DeepSeek Chat / DeepSeek Reasoner
- **文档处理**：python-docx
- **Web 服务器**：Waitress（生产环境）
- **容器化**：Docker & Docker Compose

---

## ❓ 常见问题

### 1. 如何获取 DeepSeek API Key？

访问 [DeepSeek 官网](https://platform.deepseek.com/)，注册账号后在控制台创建 API Key。

### 2. 支持哪些 AI 模型？

- `deepseek-chat`：标准模式，适合日常对话和内容生成
- `deepseek-reasoner`：思考模式，具备更强的逻辑推理能力

在管理后台可以切换模型。

### 3. 生成的文档保存在哪里？

所有生成的 Word 文档保存在 `output/` 目录，文件名格式为：
`YYYYMMDD_HHMM_课题名称_v版本号.docx`

### 4. Docker 部署时端口冲突怎么办？

修改 `.env` 文件中的端口配置：

```bash
PORT=8080  # 将端口改为 8080
```

或修改 `docker-compose.yml` 中的端口映射：

```yaml
ports:
  - "8080:9998"  # 将本地端口改为 8080，容器内保持 9998
```

### 5. 如何更新配置不重启容器？

**配置分两类：**

1. **环境变量配置**（`.env` 文件）：需要重启容器

   ```bash
   docker-compose down
   docker-compose up -d
   ```
2. **运行时配置**（管理后台修改）：立即生效，无需重启

### 6. 忘记了管理员密码怎么办？

编辑 `.env` 文件，修改 `ADMIN_PASSWORD` 和 `WEB_ACCESS_PASSWORD`，然后重启应用：

```bash
# Docker 部署
docker-compose restart

# 本地运行
# 停止程序后重新运行 python A3.py
```

---

## 📝 更新日志

### v1.0.0 (2025-10-15)

- ✨ 初始版本发布
- ✅ 完整的 A3 报告 8 步骤支持
- ✅ AI 实时验证和多轮对话
- ✅ 管理员配置后台
- ✅ Docker 部署支持
- ✅ 权限管理系统

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

如有问题或建议，请联系项目维护者。

---

## 🌟 致谢

- DeepSeek AI 提供强大的 AI 能力
- Flask 社区提供优秀的 Web 框架
- 所有精益管理和 A3 方法论的研究者和实践者

---

**开始使用 A3 报告助手，让 AI 助力精益改进！** 🚀
