# A3 报告改善助手 v1.0.0

## 项目概述

基于Flask和DeepSeek AI的智能A3改善报告生成工具，支持在线配置、智能建议、管理员权限控制和防重复生成等高级功能。

## 核心特性

### 1. 智能报告生成

- **AI智能检查**: 基于DeepSeek AI模型的专业A3方法指导
- **追问互动**: 支持用户与AI深度交流，获取针对性建议
- **Word文档输出**: 自动生成专业格式的A3改善报告Word文档
- **实时提示**: 生成过程中显示进度模态框，防止重复操作

### 2. 管理员配置系统

- **安全访问控制**: 管理员页面需要密码验证（默认：admin123）
- **API配置管理**: 在线配置DeepSeek API Key和Base URL
- **模型选择**: 支持标准模式(deepseek-chat)和思考模式(deepseek-reasoner)
- **文档样式设置**: 自定义生成Word文档的字体和标题模板
- **系统提示词管理**: 可视化编辑AI的各种角色设定和提示词
- **A3步骤管理**: 动态添加、编辑、删除A3报告步骤流程

### 3. 用户体验优化

- **响应式设计**: 支持桌面和移动设备的完美适配
- **主题一致性**: 统一的视觉设计和交互体验
- **防重复点击**: 智能缓冲机制防止重复生成任务
- **自动保存**: 表单内容自动保存到本地存储
- **错误处理**: 完善的错误提示和异常处理机制

### 4. 技术架构升级

- **模板分离**: HTML模板独立管理，支持Flask标准模板引擎
- **会话管理**: 基于Flask Session的安全会话控制
- **AJAX交互**: 无刷新的文件生成和下载体验
- **任务去重**: 基于哈希和时间戳的任务ID防重复机制

## 版本历史

### v1.0.0 (当前版本)

- ✅ 新增管理员密码保护功能
- ✅ 实现生成过程模态框提示
- ✅ 优化AJAX文件下载体验
- ✅ 完善防重复点击机制
- ✅ 移除主题切换功能，统一界面风格
- ✅ 修复回车键触发逻辑，仅支持追问功能

## 快速开始

### 环境要求

- Python 3.8+
- Flask
- python-docx
- openai
- waitress (生产环境)

### 安装部署

#### 方式一：直接运行

```bash
# 1. 克隆项目
git clone <repository-url>
cd A3报告助手

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置API Key（可选，也可在管理页面配置）
# 编辑 config.py 文件，设置 DEEPSEEK_API_KEY

# 4. 启动应用
python A3.py

# 5. 访问应用
# 浏览器打开 http://localhost:9998
```

#### 方式二：Docker部署

```bash
# 1. 构建镜像
docker build -t a3-assistant .

# 2. 运行容器
docker run -d \
  --name a3-assistant \
  -p 9998:9998 \
  -e DEEPSEEK_API_KEY=your_api_key \
  -v $(pwd)/output:/app/output \
  a3-assistant

# 3. 使用docker-compose（推荐）
docker-compose up -d
```

### 使用指南

#### 1. 首次配置

1. 访问 `http://localhost:9998`
2. 点击右上角"管理配置"按钮
3. 输入管理员密码：`admin123`
4. 配置DeepSeek API Key和其他参数
5. 保存配置并返回主页

#### 2. 生成A3报告

1. 在主页按照8个步骤填写内容
2. 使用"AI智能检查"获取专业建议
3. 通过"追问"功能深入交流
4. 点击"生成Word报告"下载最终文档

#### 3. 管理员功能

- **API配置**: 设置DeepSeek API密钥和服务地址
- **模型选择**: 选择标准模式或思考模式
- **提示词管理**: 自定义AI的角色设定和回复风格
- **步骤管理**: 编辑A3报告的步骤流程
- **文档设置**: 配置输出Word文档的格式

## 文件结构

```
A3报告助手/
├── A3.py                     # 主程序文件
├── config.py                 # 配置文件
├── requirements.txt          # Python依赖
├── Dockerfile               # Docker构建文件
├── docker-compose.yml       # Docker Compose配置
├── README.md               # 项目说明
├── templates/              # 模板文件夹
│   ├── index.html          # 主页面模板
│   ├── admin.html          # 管理员配置页面
│   └── admin_login.html    # 管理员登录页面
└── output/                 # 生成报告输出目录
```

## 配置说明

### 环境变量

- `DEEPSEEK_API_KEY`: DeepSeek API密钥
- `FLASK_ENV`: Flask运行环境 (development/production)
- `PYTHONUNBUFFERED`: Python输出缓冲控制

### 主要配置项

```python
# API配置
DEEPSEEK_API_KEY = "your-api-key"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"  # 或 "deepseek-reasoner"

# 管理员配置
ADMIN_PASSWORD = "admin123"

# 文档配置
DOC_FONT_NAME = "宋体"
DOC_TITLE_TEMPLATE = "A3 报告优化 – {topic}"
```

## 安全注意事项

1. **API密钥保护**:

   - 生产环境请使用环境变量设置API密钥
   - 避免在代码中硬编码敏感信息
2. **管理员密码**:

   - 部署前请修改默认管理员密码
   - 建议使用强密码并定期更换
3. **网络安全**:

   - 生产环境建议使用HTTPS
   - 配置防火墙限制管理页面访问
4. **数据安全**:

   - 避免输入机密或敏感信息
   - 建议使用示例数据或脱敏内容

## 故障排除

## 许可证

本项目基于MIT许可证开源，详见LICENSE文件。

---

*A3改善报告助手 - 让精益改善更智能、更高效！*
