# High-Availability Container Orchestration with Docker Swarm

## Objectives
- Initialize a multi-node Docker Swarm cluster across Manager and Worker nodes.
- Deploy microservices stack with Docker Stack using `overlay` networking and persistent volumes.
- Execute zero-downtime horizontal scaling, dynamic service updates, and rolling rollouts.
- Verify cluster self-healing during sudden worker node failures.
- Perform zero-downtime cluster maintenance via node draining and active re-balancing.

## Tools Used
- **Orchestration:** Docker Swarm, Docker Stack, Docker CLI
- **Networking:** Swarm Overlay Driver, Ingress Load Balancing
- **Containers:** Nginx, Redis
- **OS Platform:** Ubuntu Linux, Systemd

## Key Skills Demonstrated
- Multi-node container orchestration architecture.
- Self-healing cluster management and fault tolerance.
- Declarative stack deployments via Compose specs.
- Live traffic maintenance via node draining (`drain` availability).
- Microservice load balancing across dynamic container replicas.

## Troubleshooting Log
- **Deprecation Fix:** Replaced legacy unmaintained `dockersamples/visualizer:stable` container reference with standard `dockersamples/visualizer` tag to maintain compatibility across modern Docker runtimes.
- **Node Heartbeat Diagnostics:** Verified Swarm heartbeat timeouts and automatic task redistribution when nodes enter offline state (`systemctl stop docker`).
