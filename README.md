# Telecom AI API - DevOps Demo

A production-style FastAPI service for a Telecom operator, with full CI/CD, Docker, Kubernetes, Autoscaling and Monitoring.

Built to demonstrate: **CI/CD -> Docker -> Kubernetes -> Self-Healing -> Rollback**

## Tech Stack
- **API:** FastAPI + Python 3.11
- **CI/CD:** GitHub Actions + pytest + Trivy Security Scan
- **Container:** Docker
- **Orchestration:** Kubernetes (kind) - Deployment, Service, ConfigMap, Secret, HPA
- **Monitoring:** Prometheus + Grafana

## Architecture
git push -> GitHub Actions (test + scan + build) -> Docker Image -> Kubernetes Deployment (2 replicas) -> Service -> HPA (2-5 pods)

## API Endpoints
| Endpoint | Description |
| :--- | :--- |
| `GET /health` | Health check for K8s probes |
| `GET /subscriber/{id}` | Get subscriber plan & status |
| `POST /support` | AI Agent - creates support ticket from query |

## Quick Start - Local
```bash
docker build -t telecom-ai-api .
docker run -p 8000:8000 telecom-ai-api
curl http://localhost:8000/health
Quick Start - Kubernetes (Day 2)
kind create cluster --name telecom-demo
docker build -t telecom-ai-api .
kind load docker-image telecom-ai-api --name telecom-demo
kubectl apply -f k8s/
kubectl get pods
kubectl port-forward svc/telecom-ai-api 8080:80
curl http://localhost:8080/health
What I Verified
CI pipeline green on every push to mainTrivy scan for Docker image vulnerabilities2 pods running with liveness + readiness probesSelf-healing: Deleted pod auto-recreated by K8sManual scale: 2 -> 4 -> 2 pods verifiedRollback: kubectl rollout undo verifiedHPA: Autoscale 2-5 pods on 70% CPUCommands for Demobashkubectl get pods
kubectl delete pod <pod-name> # watch it self-heal
kubectl scale deployment telecom-ai-api --replicas=4
kubectl rollout undo deployment/telecom-ai-apiProject Structurejavascriptapp/main.py - FastAPI app
tests/ - pytest
Dockerfile
.github/workflows/ci-cd.yml - CI pipeline
k8s/ - deployment, service, configmap, secret, hpa 
