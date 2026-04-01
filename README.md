# aks-monitoring-infra
This repository contains a reference DevOps implementation for a hybrid monitoring platform running on Azure and Kubernetes, including Infrastructure as Code, CI/CD, observability, networking, and cost optimization practices. It demonstrates my experience with Terraform/Bicep, GitHub Actions and Azure DevOps, AKS/on‑prem clusters, secure networking, and SOC 2–aligned controls.

# aks-monitoring-infra

This repository contains a reference DevOps implementation for a containerized monitoring/web API running on Azure Kubernetes Service (AKS), provisioned with Terraform and deployed via GitHub Actions, with full observability through Azure Monitor and Log Analytics.It demonstrates hands‑on experience with Infrastructure as Code, AKS workloads, CI/CD automation, and production‑style monitoring and alerting on Azure

## Technologies

- Azure: Resource Groups, Virtual Network and subnets, Azure Kubernetes Service (AKS), Azure Container Registry (ACR), Azure Monitor, Log Analytics workspace, Application Insights
- Infrastructure as Code: Terraform modules for networking, AKS cluster, ACR, and monitoring resources.
- CI/CD: GitHub Actions workflows to build and test Docker images, scan them, push to ACR, and deploy to AKS using `kubectl`/Helm
- Observability: Azure Monitor and Log Analytics‑based metrics, logs, and alerts for cluster and application health (CPU, memory, error rate, latency)

## What this project demonstrates

- **Infrastructure as Code:** Declarative Terraform configuration to provision Azure networking, AKS, container registry, and monitoring resources in a repeatable way across environments (dev/prod)
- **CI/CD pipelines:** Automated build‑test‑deploy pipeline in GitHub Actions, including image build, basic checks, and rollout of new versions to AKS.
- **AKS deployment:** A sample Dockerized application deployed to AKS with readiness/liveness probes and environment‑specific configuration and secrets.
- **Monitoring and alerting:** Integration with Azure Monitor and Log Analytics, with example alert rules for resource saturation and application reliability
## Repository structure

- `infra/` – Terraform configuration for resource groups, networking, AKS, ACR, and monitoring resources
- `.github/workflows/` – GitHub Actions workflows for CI/CD and (optionally) infrastructure changes
- `app/` – Sample containerized application and Kubernetes manifests/Helm chart for deploying to AKS
- `docs/architecture.md` – High‑level overview of the architecture, pipelines, and monitoring/alerting approach

## How to use

1. Configure Azure credentials and environment variables for Terraform and GitHub Actions
2. Run Terraform to provision or update the AKS infrastructure and supporting resources
3. Push changes to trigger the GitHub Actions workflows, which build and deploy the application to AKS
4. View metrics, logs, and alerts in Azure Monitor and Log Analytics to observe the system’s behavior
