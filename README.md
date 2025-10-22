
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
<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/7cdbc4d7-dac0-4fd2-80e6-3c2c66eadafe" />

The workflow also include a healthcheck curl endpoint working.
---

### 3. EC2 Deployment

* Installed Docker on EC2.
* Deployed the app using GitHub Actions.
* Verified endpoints:

```
Home: http://13.60.49.84:8080/
```
<img width="940" height="507" alt="image" src="https://github.com/user-attachments/assets/7f67550e-aef4-4e08-a10b-234788436cc2" />

---

### 4. Monitoring

* **AWS CloudWatch**: Monitors EC2 metrics and alarms. Also configured an sns topic such that the I receive any alerts thhrough email first whenever our instnace is down.
* **UptimeRobot**: Checks `/healthz` endpoint to ensure the application is online.
<img width="940" height="440" alt="image" src="https://github.com/user-attachments/assets/42c9a07b-a265-489b-8413-f026f7a18e84" />
<img width="940" height="236" alt="image" src="https://github.com/user-attachments/assets/93425f16-74b5-4f25-a420-acf5b95ebc7a" />

<img width="940" height="441" alt="image" src="https://github.com/user-attachments/assets/9055bf96-62d8-4827-90b0-a6b6be61d049" />



---

### 5. Security & Cost Optimization

* **Vulnerability Scan**:

```bash
trivy image drviki-app
```

* **Security**: Image scanning with Trivy.
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/bc0fb3b2-b740-43bb-acde-1b3393276d8b" />
<img width="940" height="528" alt="image" src="https://github.com/user-attachments/assets/471c28e3-fa2a-43f5-9695-f584f78fefa8" />


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

