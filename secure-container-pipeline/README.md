# Enterprise Container Security & Runtime Hardening

## Objectives
- Build non-root container images enforcing UID/GID privilege separation.
- Enforce immutability using read-only (`--read-only`) root filesystems and explicit `tmpfs` mounts.
- Strip Linux kernel capabilities (`--cap-drop=ALL`) and mandate `no-new-privileges` security flags.
- Scan container images for CVE vulnerabilities using automated scanner pipelines.
- Implement production-grade multi-layer security in Docker Compose stack definitions.

## Tools Used
- **Engine & Orchestration:** Docker Engine, Docker Compose
- **Security Tools:** Trivy Vulnerability Scanner, Linux Capabilities (`capsh`), AppArmor/SecurityOpt
- **Language/Framework:** Python 3.9, Flask, Alpine Linux

## Key Skills Demonstrated
- Zero-Trust container security architecture and attack surface minimization.
- Immutable infrastructure deployment using read-only filesystems.
- Privilege escalation prevention (`no-new-privileges` and non-root execution).
- Container vulnerability management and base-image minimization.

## Troubleshooting Log
- **Automated Sandbox Compatibility:** Substituted interactive `docker trust` passphrase prompts with local registry tagging, and utilized Trivy for headless offline CVE scanning inside sandbox environments.
- **Read-Only App Storage Fix:** Mounted an explicit size-capped `tmpfs` volume (`/tmp:rw,noexec,nosuid`) to allow necessary ephemeral application writes without compromising root filesystem immutability.
