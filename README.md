# 🚀 CloudForge — Automated Cloud-Native DevSecOps & Observability Platform

**CloudForge** is an end-to-end Cloud-Native deployment platform designed to demonstrate modern **CI/CD**, **DevSecOps**, **Kubernetes Orchestration**, and **Full-Stack Observability**. It automates the build, security verification, container registry publishing, and zero-downtime deployment of a containerized Python Flask microservice.

### ✨ Key Highlights
* **Automated CI/CD Pipeline:** Powered by GitHub Actions to automate linting, testing, image building, and publishing to GitHub Container Registry (GHCR) using immutable commit SHA tags.
* **Shift-Left DevSecOps:** Integrated **Trivy** scanning for filesystem vulnerabilities, secrets detection, and Kubernetes manifest misconfigurations (`securityContext` hardening, non-privilege escalation, and read-only root filesystems).
* **Resilient Kubernetes Orchestration:** Deployed with zero-downtime `RollingUpdate` strategies, readiness/liveness health probes (`/healthz`), resource quotas, Nginx Ingress routing, and automated rollout verification with instant failure rollback.
* **Real-Time Observability:** Instrumented with **Prometheus** metrics and visualized through custom **Grafana** dashboards tracking HTTP request rates, latency, and pod-level CPU/memory lifecycles.
