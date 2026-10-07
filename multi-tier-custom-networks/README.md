# Advanced Docker Networking & Multi-Tier Traffic Isolation

## Objectives
- Construct custom Docker bridge networks with user-defined IPAM CIDR subnets.
- Implement multi-tier application security using dual-homed container routing.
- Verify embedded DNS service discovery across user-defined bridge drivers.
- Evaluate host network performance (`--network host`) vs isolated null networks (`--network none`).
- Execute real-time dynamic network interface hot-plugging (`connect` and `disconnect`).

## Tools Used
- **Engine:** Docker Engine, Docker CLI
- **Networking Drivers:** Bridge, Host, None, IPAM
- **Inspection Tools:** `iptables`, `ip route`, `ip addr`, Docker Inspect
- **Containers:** Nginx Alpine, MySQL 8.0, Alpine Linux

## Key Skills Demonstrated
- Microservice network segmentation and zero-trust container isolation.
- Embedded DNS service discovery design without hardcoded static IPs.
- Dual-homed network architecture for secure backend gateway services.
- Advanced network diagnostics and IPTables NAT forwarding inspection.

## Troubleshooting Log
- **Syntax Conflict Fix:** Resolved `--network host` and `-p` port-mapping conflict where Docker CLI ignores port mapping under host driver mode; removed redundant port flags to bind directly to host interfaces.
- **Targeted Container Cleanup:** Replaced destructive `docker stop $(docker ps -q)` ancestor cleanup filters with explicit container names to avoid accidentally tearing down active web/database services.
