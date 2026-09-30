# Lab 7: Docker Compose - Multi-Container Applications

## 📌 Overview
This repository contains the setup for **Lab 7: Docker Compose**, demonstrating how to define, run, scale, and manage multi-container applications using `docker-compose.yml`.

## 🏗️ Architecture
- **Web Server:** Nginx (Alpine-based) serving custom HTML content on port `8080`.
- **Database:** MySQL 8.0 with pre-loaded initialization scripts via SQL entrypoint volume mounting.
- **Load Balancer (Scalable Stack):** Nginx reverse proxy routing traffic across dynamically scaled web instances.
- **Networking & Volumes:** Custom isolated bridge network (`app-network`) and persistent storage volume (`mysql-data`).

## 🚀 Quick Start Instructions

### 1. Standard Multi-Container Stack


Launch the stack in detached mode

docker-compose up -d

Verify running services
docker-compose ps

Check application output
curl http://localhost:8080

Verify MySQL database query execution
docker-compose exec database mysql -u appuser -papppassword123 -e "SELECT * FROM sampleapp.users;"

Teardown standard stack
docker-compose down -v

### 2. Scalable Multi-Container Stack with Load Balancing

Start scalable stack with 3 instances of webserver
docker-compose -f docker-compose-scalable.yml up -d --scale webserver=3

Inspect running webserver instances
docker-compose -f docker-compose-scalable.yml ps

Teardown scalable stack and remove volumes
docker-compose -f docker-compose-scalable.yml down -v


## 🛠️ Verification Checklist
- [x] Docker Compose configured and verified
- [x] Web server serving custom index page on port 8080
- [x] Database seeded automatically via `/docker-entrypoint-initdb.d`
- [x] Dynamic service scaling with custom Nginx reverse proxy
- [x] Clean resource cleanup verification (`docker-compose down -v`)
