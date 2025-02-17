import os
from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_IMAGE = os.path.join(BASE_DIR, "test_images", "neurolab.png")

def test_detect_objects():
    with open(TEST_IMAGE, "rb") as file:
        response = client.post("/detect/", files={"file": file})
        assert response.status_code == 200
        assert "detections" in response.json()
