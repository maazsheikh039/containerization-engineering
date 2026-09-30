# Automated Custom Container Build Engine & Security Hardening

## 📌 Executive Summary
This repository contains an enterprise-grade demonstration of building custom container images from scratch using Dockerfiles. It highlights **Layer Caching Optimization**, **Non-Root Security Hardening**, **Environment Variable Injection**, and **Embedded Runtime Health Checks** for a Python Web Application.

---

## 🏗️ Architecture & Dockerfile Construction Model

```text
+-------------------------------------------------------------------------+
|                          DOCKER BUILD CONTEXT                           |
|                                                                         |
|  [FROM python:3.11-slim]      <-- Base Minimal Linux OS & Python Runtime |
|  [COPY requirements.txt]      <-- Dependency Caching Layer              |
|  [RUN pip install...]         <-- Execute Dependency Setup              |
|  [COPY app/ .]                <-- Application Source Code Copy          |
|  [RUN useradd appuser]        <-- Security Hardening (Non-Root User)    |
|  [USER appuser]               <-- Privilege Reduction Switch            |
|  [HEALTHCHECK Instruction]    <-- Automated Health Check                |
|  [CMD ["python", "app.py"]]   <-- Default Container Entry Point         |
+-------------------------------------------------------------------------+

🛠️ Key Technical Best Practices Applied
Layer Caching Optimization: requirements.txt is copied and installed prior to copying the application source code. This prevents unnecessary dependency re-installs during source code changes.

Principle of Least Privilege: Default containers run as root. This configuration provisions a dedicated restricted system user (appuser) and group to mitigate container breakout threats.

Runtime Configuration Flexibility: Uses ENV directives combined with os.environ calls in Python to allow runtime environment overrides via -e or Compose configurations.


