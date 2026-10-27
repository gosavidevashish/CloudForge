# DevSecOps & Kubernetes End-to-End Demo.

This repository contains the complete codebase, Docker setup, Kubernetes manifests, and GitHub Actions CI/CD automation pipeline.

## Repository Layout
- `app/`: Flask application source code.
- `tests/`: Automated unit tests.
- `k8s/`: Kubernetes manifests (Namespace, Deployment, Service, ConfigMap, Secret).
- `.github/workflows/`: Automated DevSecOps & K8s deployment pipeline.

## Quickstart
1. Replace `YOUR_GITHUB_USERNAME` and `YOUR_REPO_NAME` in `k8s/deployment.yaml` with your actual repo details.
2. Add your cluster `kubeconfig` as a GitHub Secret named `KUBE_CONFIG`.
3. Push to `main` branch to trigger CI/CD pipeline.
