# 使用官方 Python 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装 Python 包
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制应用代码
COPY . .

# 创建非root用户
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 创建必要的目录并设置权限
RUN mkdir -p output logs && \
    chmod 755 /app && \
    chmod 644 /app/*.py && \
    chmod 755 /app/templates && \
    chmod 644 /app/templates/* && \
    chown -R appuser:appuser /app

# 切换到非root用户
USER appuser

# 设置环境变量
ENV FLASK_APP=A3.py \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1

# 暴露端口
EXPOSE 9998

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:9998/', timeout=5)" || exit 1

# 启动命令
CMD ["python", "A3.py"]