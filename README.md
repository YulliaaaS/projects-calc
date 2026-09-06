
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

```

---

## Tech Stack

* **Cloud Provider:** AWS (EC2, Security Groups)
* **Infrastructure as Code (IaC):** Terraform
* **Containerization:** Docker, Docker Compose
* **CI/CD Pipeline:** GitHub Actions
* **Backend & Frontend:** Python 3.10, Flask, HTML5/CSS3
* **Web Server Interaction:** REST API (JSON communication between microservices)

---

## Features

* **Microservices Architecture:** Decoupled Frontend (UI/Routing) and Backend (Calculation API).
* **Automated CI/CD:** Every push to the `main` branch automatically triggers code deployment onto the remote AWS EC2 instance without downtime.
* **Infrastructure Management:** EC2 instances and security group rules are managed reproducibly via Terraform.
* **Isolated Environment:** Services run inside isolated Docker containers connected via a private Docker bridge network.

---

## How to Run Locally

### Prerequisites

* Docker & Docker Compose installed
* Git installed

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/YulliaaaS/projects-calc.git
cd projects-calc

```


2. **Run with Docker Compose:**
```bash
docker compose up -d --build

```


3. **Access the application:**
Open your browser and navigate to `http://localhost:5000`

---

## Security & Deployment Notes

* All SSH keys and sensitive variables (host IPs, usernames) are securely stored using **GitHub Actions Secrets**.
* Port `5000` is exposed for user access, while internal microservice communication occurs within the internal container network.

```

Після збереження файла відправте оновлення на GitHub:

```powershell
git add README.md
git commit -m "Fix markdown code block closing in README"
git push origin main

```