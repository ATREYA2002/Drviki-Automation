DevOps Pipeline DrViki Flask web application

This repository demonstrates a complete DevOps workflow for a Flask web application, from containerization to automated deployment, monitoring, and security scanning.

Overview

Dr. ViKi is a sample Flask application that:

Serves a home page with timestamp.

<img width="858" height="286" alt="image" src="https://github.com/user-attachments/assets/8260c8b4-4d07-496d-9d1a-492e21fb21fd" />

The application is containerized with Docker and deployed on AWS EC2 using GitHub Actions CI/CD. Monitoring and security scanning are integrated.

Step-by-Step Workflow
1. Dockerize Locally

Containerized the Flask app using a Dockerfile.

Built the image locally:

docker build -t drviki-app .


Tested the container locally on localhost:8080:

docker run -d -p 8080:8080 --name drviki-app drviki-app
curl http://localhost:8080

2. GitHub Actions Workflow

Created a workflow in .github/workflows/aws.yml to automate CI/CD:

Key steps:

Checkout repository.

Build Docker image.

Run container and test endpoints.

Deploy to EC2 instance using SSH and SCP.

Replace the previous container if running.

This ensures seamless, automated deployment whenever code is pushed to main.

3. EC2 Deployment

Installed Docker on EC2.

Deployed the app using GitHub Actions.

Verified endpoints:

http://<EC2_PUBLIC_IP>:8080/

4. Monitoring

AWS CloudWatch: Monitors EC2 uptime and logs.

UptimeRobot: Checks /healthz endpoint to ensure the application is online.

Prometheus Metrics: Exposed at /metrics to track request counts.

5. Security & Cost Optimization

Vulnerability Scan:

trivy image drviki-app


Image scanning with Trivy reduces known vulnerabilities.

Repo Structure
Drviki-Automation/
├── app.py
├── dockerfile
├── requirements.txt
├── README.md
└── .github/workflows/
    └── aws.yml
