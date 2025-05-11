from fastapi import WebSocket
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_websocket_connection(client: TestClient):
    with client.websocket_connect("/ws/market-data") as websocket:
        assert websocket is not None

@pytest.mark.asyncio
async def test_subscribe_market_data(client: TestClient):
    with client.websocket_connect("/ws/market-data") as websocket:
        websocket.send_text("subscribe:BTC")
        response = websocket.receive_text()
        assert response == "Subscribed to BTC market data"

@pytest.mark.asyncio
async def test_unsubscribe_market_data(client: TestClient):
    with client.websocket_connect("/ws/market-data") as websocket:
        websocket.send_text("unsubscribe:BTC")
        response = websocket.receive_text()
        assert response == "Unsubscribed from BTC market data"

@pytest.mark.asyncio
async def test_invalid_subscription(client: TestClient):
    with client.websocket_connect("/ws/market-data") as websocket:
        websocket.send_text("subscribe:INVALID")
        response = websocket.receive_text()
        assert response == "Invalid market data subscription"