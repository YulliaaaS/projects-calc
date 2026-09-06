# Two-Tier Flask Calculator Application (DevOps Project)

A fully automated, two-tier microservice web application built with Python (Flask), containerized using Docker, and deployed to AWS EC2 via GitHub Actions CI/CD pipeline. The underlying infrastructure is provisioned using Infrastructure as Code (IaC) with Terraform.

---

## Architecture Diagram

```text
[ Developer ]
      │
   git push
      │
      ▼
[ GitHub Actions CI/CD Pipeline ]
      │ (SSH Deployment)
      ▼
┌─────────────────────────────────────────────────────────────┐
│ AWS EC2 Instance (eu-north-1)                               │
│                                                             │
│  ┌───────────────────────┐       ┌───────────────────────┐  │
│  │  Frontend Container   │ ────► │   Backend Container   │  │
│  │   (Flask / Port 5000) │  HTTP │   (Flask / Port 5001) │  │
│  └───────────────────────┘       └───────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
      ▲
      │ HTTP Request
[ End User ]