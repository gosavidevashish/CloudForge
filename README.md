# 🚀 CloudForge

An end-to-end Cloud-Native DevSecOps platform automating the build, security scanning, zero-downtime Kubernetes deployment, and real-time observability of a containerized Python Flask microservice.

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD%20Pipeline-Passing-brightgreen?logo=github)](https://github.com/gosavidevashish/CloudForge/actions)
[![Security: Trivy](https://img.shields.io/badge/Security-Trivy%20Scanned-yellow?logo=aquasecurity)](#)
[![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5?logo=kubernetes&logoColor=white)](#)
[![License: Unlicense](https://img.shields.io/badge/License-Unlicense-orange.svg)](https://unlicense.org/)

---

## 📝 Overview
**CloudForge** is a production-grade DevSecOps reference architecture designed to eliminate manual deployment bottlenecks, unverified container releases, and infrastructure blind spots. It integrates automated GitHub Actions workflows with shift-left **Trivy** security gates to ensure only vulnerability-free, hardened containers reach the Kubernetes cluster. Once deployed, **Prometheus** and **Grafana** provide full-stack visibility into application traffic, latency, and pod-level resource consumption.

### 🖼️ Demo & Architecture Screenshots

#### 🔄 Automated CI/CD Pipeline
<img width="1412" height="300" alt="Screenshot 2026-11-01 021438" src="https://github.com/user-attachments/assets/fdf58fab-01f2-4c1f-9cc1-bf7f547fafa9" />

#### 🛡️ Trivy DevSecOps Scan (0 Issues)
<img width="737" height="522" alt="Screenshot 2026-11-01 021654" src="https://github.com/user-attachments/assets/f2b7e167-dd00-45ff-86eb-84b08c23b8b2" />

#### 📊 Grafana Real-Time Observability
<img width="1510" height="902" alt="Screenshot 2026-11-01 022614" src="https://github.com/user-attachments/assets/715c451d-9786-46e9-8701-0691ffa839f6" />

#### ☸️ Kubernetes Cluster & Pod Status
<img width="780" height="67" alt="Screenshot 2026-11-01 023313" src="https://github.com/user-attachments/assets/a2000a48-5522-40c9-b021-a6da9264c495" />

#### 🌐 Live Microservice Output (`/`)
<img width="1370" height="123" alt="Screenshot 2026-11-01 023431" src="https://github.com/user-attachments/assets/cc537b7a-48e7-4ee0-897e-3454df7e0983" />

#### ❤️ Health Probe Output (`/health`)
<img width="1370" height="123" alt="Screenshot 2026-11-01 023411" src="https://github.com/user-attachments/assets/50d40adc-020f-4483-ae40-0ea40268d9ec" />

---

## ⚡ Key Features
- **Automated CI/CD with Self-Healing Rollbacks:** Builds immutable Docker images tagged with commit SHAs, publishes to GitHub Container Registry (GHCR), deploys to Kubernetes, and automatically triggers a rollback if a rollout times out or fails health checks.
- **Shift-Left DevSecOps (Trivy Integration):** Automatically scans application dependencies, Dockerfiles, secrets, and Kubernetes manifests for CVEs and misconfigurations before deployment.
- **Hardened Kubernetes Orchestration:** Configured with strict `securityContext` policies (`readOnlyRootFilesystem: true`, dropped `ALL` Linux capabilities, disabled privilege escalation), resource requests/limits, Nginx Ingress routing, and liveness/readiness probes (`/healthz`).
- **Full-Stack Observability:** Out-of-the-box **Prometheus** scraping (`PodMonitor`) and pre-configured **Grafana** dashboards tracking live HTTP request rates, cumulative traffic, and pod CPU/memory lifecycles.

---

## 🛠️ Tech Stack

| Category | Technology Used |
| --- | --- |
| **Backend / App** | Python 3, Flask, Gunicorn, Prometheus Flask Exporter |
| **Container & Registry** | Docker, GitHub Container Registry (GHCR) |
| **Orchestration** | Kubernetes (Minikube), Nginx Ingress Controller |
| **CI/CD & Security** | GitHub Actions (Self-Hosted Runner), Aqua Trivy |
| **Observability** | Prometheus (`kube-prometheus-stack`), Grafana, PromQL |

---

## 🚀 Getting Started

Follow these steps to set up the project locally for development, cluster deployment, and monitoring.

### 📋 Prerequisites
Ensure you have the following installed on your local machine:
- Docker Desktop
- Minikube & `kubectl`
- Helm (v3+)
- Python (v3.10 or higher)
- Git

### 🔧 Installation & Setup
Run the following commands in your terminal:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/gosavidevashish/CloudForge.git](https://github.com/gosavidevashish/CloudForge.git)
   cd CloudForge

2. **Start the Kubernetes cluster & enable Ingress:**
   ```powershell
   minikube start
   minikube addons enable ingress
   ```

3. **Deploy the Kubernetes manifests:**
   ```powershell
   kubectl apply -f CloudForge/k8s/namespace.yaml
   kubectl apply -f CloudForge/k8s/configmap.yaml
   kubectl apply -f CloudForge/k8s/secret.example.yaml
   kubectl apply -f CloudForge/k8s/deployment.yaml
   kubectl apply -f CloudForge/k8s/service.yaml
   kubectl apply -f CloudForge/k8s/ingress.yaml
   ```

4. **Verify pod status and port-forward the application:**
   ```powershell
   kubectl get pods -n devops-demo
   kubectl port-forward svc/demo-app-service 5000:80 -n devops-demo
   ```
   - **App Endpoint:** `http://localhost:5000/`
   - **Health Probe:** `http://localhost:5000/healthz`

5. **Access the Grafana Observability Dashboard:**
   ```powershell
   kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
   ```
   - Open `http://localhost:3000` in your browser (Default login: `admin` / `prom-operator`).

---

## 🤝 Contributing
Contributions make the open-source community an amazing place to learn and create.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License
Distributed under the "The Unlicense". See `LICENSE` for more information.

---

## 👥 Authors & Contact
- **Devashish Gosavi** - [@gosavidevashish](https://github.com/gosavidevashish)
- **Project Link:** [https://github.com/gosavidevashish/CloudForge](https://github.com/gosavidevashish/CloudForge)
