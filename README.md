
# System Monitoring

System Monitoring is a web application that provides real-time monitoring of CPU and memory usage on a system. It uses Flask, Chart.js, and psutil to fetch system metrics and visualize them in the form of line charts.

## Features

- Real-time monitoring of CPU and memory usage.
- Two line charts displaying CPU and memory usage over time.
- Automatic updates every second to reflect the latest system metrics.
- Scalable deployment using Docker and Kubernetes.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.9 or later
- Flask
- Chart.js
- psutil
- boto3
- kubernetes
- Docker 
- Kubernetes cluster

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Mostafakhalil21/MonitoringApp.git
   cd MonitoringApp
   ```

2. Install the Python dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```
   flask run
   ```

2. Open your web browser and navigate to `http://localhost:5000` to view the system monitoring dashboard.

## Deployment

To deploy the System Monitoring application to a Docker container and a Kubernetes cluster, follow these steps:

1. Build the Docker image:

   ```
   docker build -t my-monitor-app .
   ```

2. Push the Docker image to a container registry (e.g., Amazon ECR):

   ```
   docker tag my-monitor-app:latest <your-registry-uri>/my-monitor-app:latest
   docker push <your-registry-uri>/my-monitor-app:latest
   ```

3. Create a deployment and service in your Kubernetes cluster:

- run k8s.python file.
- check .
```
kubectl get deployment -n default (check deployments)
kubectl get service -n default (check service)
kubectl get pods -n default (to check the pods)
```

4. Access the deployed application using the assigned service endpoint:

```
kubectl port-forward service/<service_name> 5000:5000
```
