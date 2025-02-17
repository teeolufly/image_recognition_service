# **Image Recognition Web Service - README**

## **Overview**
This project provides an **image recognition API** using the **YOLOv8 model** and **FastAPI**. The API allows users to upload images and receive object detection results.

## **Features**
- Object detection using **YOLOv8**
- FastAPI web service with an HTTP endpoint
- Dockerized for easy deployment
- Kubernetes Helm deployment
- Testing with pytest

---

## **How to Run the Application**
This guide explains how to set up and run the **YOLOv8 Image Recognition Web Service** locally, in a **Docker container**, and on **Kubernetes using Minikube**.

---

### **Prerequisites**

Make sure you have the following installed before running the application:

- Python 3.9+ (Required for running the application locally in a virtual environment)

To run the application in kubernetes:

- Docker 
- kubectl 
- Minikube or other Kubernetes service (eg EKS)
- Helm 


## ** Running Locally**

### **Extract the Application Files**
Since the application is provided as a **zipped file**, follow these steps:

```bash
unzip ir-websvc.zip
cd ir-websvc
```

### **Set Up a Virtual Environment**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```

### **Install Dependencies**
1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### **Run the Application**
1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
2. The application will be available at:
   ```
   http://127.0.0.1:8000
   ```

### **Test the Endpoint**
1. Use `curl` or Postman to test the `/detect/` endpoint:
   ```bash
   curl -X 'POST' "http://127.0.0.1:8000/detect/" -F "file=@tests/test_images/neurolab.png"
   ```
2. The healthcheck endpoint is exposed in /health and can be checked with a GET request
   ```bash
   curl -X 'GET' "http://127.0.0.1:8000/health"
   ```

---

## ** Running in Docker**

### **Build the Docker Image**
1. Build the Docker image:
   ```bash
   docker build -t ir_websvc .
   ```

### **Run the Docker Container**
1. Run the container:
   ```bash
   docker run -p 8000:8000 ir_websvc
   ```
2. The application will be available at:
   ```
   http://127.0.0.1:8000
   ```

### **Test the Endpoint**
Use `curl` or Postman to test the `/detect/` endpoint:
   ```bash
   curl -X 'POST' "http://127.0.0.1:8000/detect/" -F "file=@tests/test_images/neurolab.png"
   ```

---

## **Running on Kubernetes (Minikube)**
Check that Minikube is running:
   ```bash
   kubectl get nodes
   ```

### ***Build the Docker Image Inside Minikube**

```bash
eval $(minikube docker-env)
docker build -t ir-websvc .
```

### Deploy the Application with Helm**
1. Navigate to the Helm chart directory:
   ```bash
   cd ir-websvc-chart
   ```

2. Install the Helm chart:
   ```bash
   helm install ir-websvc .
   ```

3. Verify that the application is running:
   ```bash
   kubectl get pods
   ```

### **Expose the Service**

```bash
minikube service ir-web-service-svc --url
```

### **Test the Endpoint**
1. Use `curl` or Postman to test the `/detect/` endpoint:
   ```bash
   curl -X 'POST' "http://192.168.49.2:31234/detect/" -F "file=@tests/test_images/neurolab.png"
   ```

---

## ** Example **
Sample Images are in the tests/test_images directory.

```bash
curl -X 'POST' "http://127.0.0.1:8000/detect/" -F "file=@tests/test_images/neurolab.png"
```

### ** Response: **
```json
{
  "detections": [
    {
      "class": "sports ball",
      "confidence": 0.44116872549057007,
      "bbox": [[45.65, 116.25, 58.23, 129.19]]
    },
    {
      "class": "frisbee",
      "confidence": 0.3896474838256836,
      "bbox": [[75.12, 60.46, 94.59, 79.90]]
    },
    {
      "class": "traffic light",
      "confidence": 0.3602575957775116,
      "bbox": [[125.33, 97.13, 147.81, 131.67]]
    },
    {
      "class": "frisbee",
      "confidence": 0.27401402592658997,
      "bbox": [[45.67, 116.17, 58.15, 129.15]]
    }
  ]
}
```

### ** Unit test **
To verify that the API is working correctly, you can also run the provided unit test from the project root directory
```bash
    PYTHONPATH=$(pwd) pytest tests/test.py -v
```
