from typing import Callable, Dict, Any
from fastapi import WebSocket

class MarketDataEvent:
    def __init__(self):
        self.subscribers: Dict[str, Callable[[Any], None]] = {}

    def subscribe(self, client_id: str, callback: Callable[[Any], None]) -> None:
        self.subscribers[client_id] = callback

    def unsubscribe(self, client_id: str) -> None:
        if client_id in self.subscribers:
            del self.subscribers[client_id]

    def publish(self, data: Any) -> None:
        for callback in self.subscribers.values():
            callback(data)

market_data_event = MarketDataEvent()