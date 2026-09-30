FROM python:3.11-slim

# Image Metadata
LABEL maintainer="student@alnafi.com"
LABEL description="Custom Python Web Application with Security Hardening"
LABEL version="2.0"

# Environment Variable Configurations
ENV APP_NAME="Dockerized Python Web App" \
    APP_VERSION="2.0.0" \
    ENVIRONMENT="production" \
    DEBUG="false" \
    PORT="8080" \
    PYTHONUNBUFFERED="1"

# Set Working Directory
WORKDIR /usr/src/app

# Copy Requirements for Layer Caching Optimization
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application Source Code
COPY app/ .
RUN chmod +x app.py

# Security Hardening: Create and run as Non-Root User
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    chown -R appuser:appuser /usr/src/app
USER appuser

EXPOSE $PORT

# Runtime Healthcheck Instruction
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT}/')" || exit 1

# Default Entrypoint Command
CMD ["python", "app.py"]
