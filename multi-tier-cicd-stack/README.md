# Multi-Service OCI Delivery Pipeline with GitLab CI/CD & Security Scanning

## Objectives
- Construct an automated 4-stage (`build`, `test`, `scan`, `deploy`) CI/CD delivery pipeline.
- Implement dual OCI image tagging using Git short SHA and semantic versioning (`VERSION`).
- Orchestrate integration testing of a 3-tier stack (Nginx proxy, Flask web microservice, Redis) via Docker Compose.
- Inject runtime database credentials using GitLab CI/CD Masked Variables with zero plaintext exposure.
- Automate container vulnerability auditing using Trivy with exported JSON scan artifacts.

## Tools Used
- **CI/CD Platform:** GitLab CI/CD, Docker-in-Docker (DinD)
- **Containerization & Orchestration:** Docker Engine, Docker Compose, Nginx Proxy
- **Security & Inspection:** Trivy Vulnerability Scanner, Masked Variables
- **Stack Technologies:** Python 3.9 Alpine, Flask, Redis 7

## Key Skills Demonstrated
- Enterprise CI/CD pipeline design with gated manual deployment steps.
- Secure secret management and zero-plaintext repository hygiene.
- Multi-service container orchestration testing in transient CI environments.
- Automated vulnerability scanning and compliance artifact generation.

## Troubleshooting Log
- **APT List Syntax Resolution:** Standardized APT sources creation for Docker and Trivy to eliminate multi-line heredoc formatting bugs (`E: Malformed entry 1`).
- **Nginx Ingress Testing:** Routed integration test healthchecks directly through Nginx reverse proxy port 80 to validate production network topologies prior to deployment.
