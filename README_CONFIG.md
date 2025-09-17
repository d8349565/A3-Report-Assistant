# A3 报告助手配置说明

## 概述
本次重构将所有配置信息统一到 `config.py` 文件中，实现了配置与业务逻辑的分离，提高了代码的可维护性和可扩展性。

## 配置文件结构

### config.py 配置项说明

#### 1. API 配置
```python
DEEPSEEK_API_KEY = "your-api-key"     # DeepSeek API 密钥
DEEPSEEK_BASE_URL = "https://api.deepseek.com"  # API 基础URL
MODEL_NAME = "deepseek-chat"          # 使用的模型名称
```

#### 2. 应用配置
```python
APP_SECRET_KEY = "A3-Assistant-Secret"  # Flask 应用密钥
OUTPUT_DIR_NAME = "output"              # 输出目录名称
```

#### 3. 文档配置
```python
DOC_FONT_NAME = "宋体"                  # Word文档字体
DOC_TITLE_TEMPLATE = "A3 改善报告 – {topic}"  # 文档标题模板
```

#### 4. AI 提示词模板
- `default`: 默认系统提示词
- `step_guidance`: 步骤指导提示词模板
- `validation`: 验证提示词模板
- `optimization`: 优化建议提示词模板

#### 5. A3 步骤指南
包含8个步骤的完整指南，每个步骤包含：
- `id`: 步骤标识符
- `title`: 步骤标题
- `purpose`: 目的说明
- `tools`: 推荐工具
- `focus`: 关注要点

#### 6. HTML 模板
完整的前端页面模板，包含CSS样式和JavaScript代码。

## 重构改进

### 1. 配置统一管理
- ✅ 所有硬编码配置移至 config.py
- ✅ 使用模板化提示词，便于修改和维护
- ✅ 分类组织配置项，结构清晰

### 2. 代码结构优化
- ✅ 移除重复的硬编码字符串
- ✅ 统一使用 config 模块导入配置
- ✅ 优化导入顺序和代码组织

### 3. 可维护性提升
- ✅ 修改配置无需修改主程序代码
- ✅ 提示词模板化，支持参数替换
- ✅ 配置项分类明确，便于管理

### 4. 错误修复
- ✅ 解决了所有未定义变量的错误
- ✅ 确保程序可以正常启动和运行
- ✅ 保持了原有功能的完整性

## 使用指南

### 修改 API 配置
在 `config.py` 中修改以下配置：
```python
DEEPSEEK_API_KEY = "your-new-api-key"
DEEPSEEK_BASE_URL = "your-api-endpoint"
MODEL_NAME = "your-model-name"
```

### 自定义提示词
在 `SYSTEM_PROMPTS` 字典中修改相应的提示词模板：
```python
SYSTEM_PROMPTS = {
    "default": "你的自定义默认提示词",
    # 其他提示词...
}
```

### 修改 A3 步骤
在 `GUIDE` 列表中修改步骤信息：
```python
GUIDE = [
    {
        "id": "step1",
        "title": "你的步骤标题",
        "purpose": "步骤目的",
        "tools": "推荐工具",
        "focus": "关注要点"
    },
    # 其他步骤...
]
```

### 自定义样式
在 `HTML_TEMPLATE` 中修改CSS样式和页面布局。

## 环境变量支持
程序支持通过环境变量设置 API Key：
```bash
export DEEPSEEK_API_KEY="your-api-key"
```

## 注意事项
1. 修改配置后需要重启程序
2. API Key 可以通过环境变量或配置文件设置
3. 提示词模板使用 Python 字符串格式化语法
4. 保持配置文件的 UTF-8 编码格式

## 测试确认
✅ 程序启动正常  
✅ 配置加载成功  
✅ 无语法错误  
✅ 功能运行正常  

通过这次重构，A3 报告助手的配置管理更加规范和灵活，为后续的功能扩展和维护奠定了良好的基础。