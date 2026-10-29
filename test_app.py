import pytest
from app import app, calculate_metrics

def test_calculate_metrics():
    total, average = calculate_metrics([80, 90, 70])
    assert total == 240
    assert average == 80.0

def test_calculate_metrics_empty():
    total, average = calculate_metrics([])
    assert total == 0
    assert average == 0

def test_web_interface_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Grade Calculator" in response.data

def test_web_interface_post_valid(client):
    response = client.post("/", data={"marks": "80, 90, 70"})
    assert response.status_code == 200
    assert b"Total Marks: 240" in response.data
    assert b"Average Marks: 80" in response.data

def test_web_interface_post_invalid(client):
    response = client.post("/", data={"marks": "-5, 110"})
    assert response.status_code == 200
    assert b"Error: Marks must be between 0 and 100" in response.data

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
