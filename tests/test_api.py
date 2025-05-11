from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_market_data():
    response = client.get("/api/market-data")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_market_data():
    response = client.post("/api/market-data", json={"symbol": "AAPL", "price": 150.0})
    assert response.status_code == 201
    assert response.json()["symbol"] == "AAPL"
    assert response.json()["price"] == 150.0

def test_invalid_market_data():
    response = client.post("/api/market-data", json={"symbol": "AAPL"})
    assert response.status_code == 422  # Unprocessable Entity for missing fields

def test_get_market_data_not_found():
    response = client.get("/api/market-data/invalid-symbol")
    assert response.status_code == 404  # Not Found for invalid symbol