# Lab 9: Dockerfile Best Practices

## 📌 Overview
This lab demonstrates industry best practices for building production-grade, secure, and minimal Docker images.

## 🎯 Key Optimization & Security Results

| Category | Unoptimized / Anti-Pattern | Best Practice Standard | Gain / Benefit |
| :--- | :--- | :--- | :--- |
| **Base Image** | `ubuntu:latest` (~220MB) | `node:18-alpine` (~170MB) | Reduced attack surface & size |
| **Layers** | 10+ individual `RUN` steps | Combined `RUN apk ... && rm -rf ...` | Reduced layer overhead |
| **Caching** | `COPY . .` before `npm install` | `COPY package*.json` first | Super-fast re-builds |
| **Multi-Stage** | Dev dependencies in image | Binary/dist copied from builder stage | Production image size cut down |
| **Security** | Default `root` user | Dedicated `USER appuser` (UID 1001) | Prevent privilege escalation |

## 🚀 Quick Execution Guide

### Build Production Master Image

docker build -f Dockerfile.production -t demo-app:production .

### Test Security & Health Check

Run container in detached mode
docker run -d --name prod-test -p 3000:3000 demo-app:production

Verify non-root user execution
docker exec prod-test whoami

Expected Output: appuser
Check health status
docker inspect --format='{{json .State.Health.Status}}' prod-test

## ✅ Verification Checklist
- [x] Official Alpine base images utilized
- [x] Multiline commands chained using `&&` and cleaned caches
- [x] Build cache strategy optimized for layer reusability
- [x] Multi-stage build isolates build tools from runtime environment
- [x] Non-root privileges (`appuser`) and Healthcheck implemented
