# Lab 8: Building and Managing Docker Images

## 📌 Overview
This lab focuses on professional Docker image creation, layer reduction optimization, multi-stage builds, `.dockerignore` context pruning, semantic tagging, and Docker Hub Registry management.

## 🎯 Key Optimization Metrics
| Build Strategy | Base Image | Approx Size | Optimization Gain |
| :--- | :--- | :--- | :--- |
| **Unoptimized** | `ubuntu:20.04` | ~220 MB | Baseline |
| **Optimized** | `nginx:alpine` | ~15-23 MB | **~90% Reduction** |
| **Multi-Stage** | `node:16-alpine` | ~110 MB | Production-only dependencies |

## 🚀 Lab Commands Quick-Reference

### 1. Layer Optimization Comparison


Unoptimized image build
docker build -f Dockerfile.unoptimized -t webapp-unoptimized:v1 .

Optimized Alpine build
docker build -f Dockerfile.optimized -t webapp-optimized:v1 .

Multi-stage Node.js build
docker build -f Dockerfile.multistage -t webapp-multistage:v1 .

Compare sizes
docker images | grep webapp

### 2. Context Pruning with .dockerignore

Build clean image excluding temp files and dev dependencies
docker build -t webapp-clean:v1 .

### 3. Tagging & Docker Hub Registry Workflow

Tagging images
docker tag webapp-clean:v1 maazsheikh039/mywebapp:1.0.0
docker tag webapp-clean:v1 maazsheikh039/mywebapp:latest

Docker Hub Push & Pull
docker push maazsheikh039/mywebapp:1.0.0
docker push maazsheikh039/mywebapp:latest

docker pull maazsheikh039/mywebapp:latest
docker run -d -p 8080:80 --name webapp-prod maazsheikh039/mywebapp:latest

## ✅ Verification Checklist
- [x] Tested Alpine vs Ubuntu image sizes
- [x] Verified Multi-stage build target isolation
- [x] Validated `.dockerignore` file exclusion
- [x] Configured Semantic version tags (`1.0.0`, `latest`, `prod`)
- [x] Successfully verified registry deployment flow
