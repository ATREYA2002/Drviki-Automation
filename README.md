Here’s your content formatted properly for a **GitHub README** using Markdown:

````markdown
# DevOps Pipeline - DrViki Flask Web Application

This repository demonstrates a complete DevOps workflow for a Flask web application, from containerization to automated deployment, monitoring, and security scanning.

---

## Overview

Dr. ViKi is a sample Flask application that:

- Serves a home page with a timestamp.
- Provides a `/healthz` endpoint for health checks.
- Exposes `/metrics` for Prometheus monitoring.

The application is containerized with Docker and deployed on AWS EC2 using GitHub Actions CI/CD. Monitoring and security scanning are integrated.

---

## Step-by-Step Workflow

### 1. Dockerize Locally

- Containerized the Flask app using a `Dockerfile`.
- Built the image locally:



```bash
docker build -t drviki-app .
````

* Tested the container locally on `localhost:8080`:

```bash
docker run -d -p 8080:8080 --name drviki-app drviki-app
curl http://localhost:8080
```
<img width="938" height="495" alt="image" src="https://github.com/user-attachments/assets/7c4f58f4-a24d-442f-84ff-c51012201236" />


---

### 2. GitHub Actions Workflow

Created a workflow in `.github/workflows/aws.yml` to automate CI/CD:

**Key steps:**

1. Checkout repository.
2. Build Docker image.
3. Run container and test endpoints.
4. Deploy to EC2 instance using SSH and SCP.
5. Replace the previous container if running.

This ensures seamless, automated deployment whenever code is pushed to `main`.

---

### 3. EC2 Deployment

* Installed Docker on EC2.
* Deployed the app using GitHub Actions.
* Verified endpoints:

```
Home: http://<EC2_PUBLIC_IP>:8080/
```

---

### 4. Monitoring

* **AWS CloudWatch**: Monitors EC2 metrics and alarms.
* **UptimeRobot**: Checks `/healthz` endpoint to ensure the application is online.


---

### 5. Security & Cost Optimization

* **Vulnerability Scan**:

```bash
trivy image drviki-app
```

* **Security**: Image scanning with Trivy reduces known vulnerabilities.
* **Cost Optimization**: Stop idle EC2 instances, use smaller instance types, or enable autoscaling for production workloads.

---

### Repo Structure

```
Drviki-Automation/
├── app.py
├── dockerfile
├── requirements.txt
├── README.md
└── .github/workflows/
    └── aws.yml
```

---

This README provides a complete walkthrough of building, deploying, monitoring, and securing the DrViki Flask application using Docker, GitHub Actions, AWS, and Trivy.

```

I can also **add badges for build status, uptime, and Trivy scan results** to make it look professional on GitHub. Do you want me to do that?
```
