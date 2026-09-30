# Docker Persistent Storage & State Management Architecture

## 📌 Technical Summary
This repository contains production-ready implementations of **Docker Storage Drivers**, **Managed Volumes**, **Stateful Container Restarts**, and **Sidecar Volume Backup & Recovery Mechanisms**. The procedures demonstrate how stateful workloads like Relational Databases (MySQL) and Web Servers preserve data integrity independent of container lifecycles.

---

## 🏗️ Technical Architecture Diagram

```text
+---------------------------------------------------------------------------------+
|                                 HOST SYSTEM                                     |
|                                                                                 |
|  +----------------------------+              +-------------------------------+  |
|  | State Container (MySQL)    |              | Sidecar Backup Container      |  |
|  | Ephemeral Execution Layer  |              | Ephemeral Backup Task (--rm)  |  |
|  +-------------+--------------+              +---------------+---------------+  |
|                |                                             |                  |
|                | Mount Path: /var/lib/mysql                  | Mount Path: /data|
|                v                                             v                  |
|  +---------------------------------------------------------------------------+  |
|  | Managed Docker Local Volume (`mysql-persistent-db`)                        |  |
|  | Physical Location: `/var/lib/docker/volumes/mysql-persistent-db/_data`    |  |
|  +---------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------+

🛠️ Key Concepts & Verification Commands
1. Ephemeral vs. Persistent Layer
Container Overlay FS: Write operations outside mounted paths are stored in the thin writable layer of the container. Removing the container deletes this layer permanently.

Managed Volumes (/var/lib/docker/volumes/): Completely managed by Docker engine on the host system, persistent across container shutdowns/deletions, and accessible by multiple containers simultaneously.

