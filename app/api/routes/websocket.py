from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List, Dict, Set

router = APIRouter()

# Store connected WebSocket clients
active_connections: List[WebSocket] = []
# Store subscriptions as symbol -> set of websockets
subscriptions: Dict[str, Set[WebSocket]] = {}
# Set of valid market symbols
valid_symbols = {"BTC", "ETH", "AAPL", "MSFT", "GOOGL"}

@router.websocket("/market-data")
async def market_data_websocket(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            
            if data.startswith("subscribe:"):
                symbol = data.split(":", 1)[1]
                if symbol in valid_symbols:
                    if symbol not in subscriptions:
                        subscriptions[symbol] = set()
                    subscriptions[symbol].add(websocket)
                    await websocket.send_text(f"Subscribed to {symbol} market data")
                else:
                    await websocket.send_text("Invalid market data subscription")
            
            elif data.startswith("unsubscribe:"):
                symbol = data.split(":", 1)[1]
                if symbol in subscriptions and websocket in subscriptions[symbol]:
                    subscriptions[symbol].remove(websocket)
                    await websocket.send_text(f"Unsubscribed from {symbol} market data")
                else:
                    await websocket.send_text(f"Unsubscribed from {symbol} market data")
            
            else:
                await websocket.send_text("Unknown command")
    except WebSocketDisconnect:
        # Remove the websocket from active connections and all subscriptions
        active_connections.remove(websocket)
        for symbol in subscriptions:
            if websocket in subscriptions[symbol]:
                subscriptions[symbol].remove(websocket)

async def broadcast_market_data(symbol: str, data: str):
    """Send market data to all clients subscribed to the symbol"""
    if symbol in subscriptions:
        for connection in subscriptions[symbol]:
            await connection.send_text(data)