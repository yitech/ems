from typing import List, Dict, Any, Optional
from app.schemas.market_data import MarketDataSchema
import datetime
import random

class MarketDataService:
    def __init__(self):
        # In-memory storage for market data
        self._market_data = {}
        # Initialize with some sample data
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        # Add some initial market data
        sample_symbols = ["BTC", "ETH", "AAPL", "MSFT", "GOOGL"]
        for symbol in sample_symbols:
            self._market_data[symbol] = MarketDataSchema(
                symbol=symbol,
                price=random.uniform(10.0, 1000.0),
                volume=random.randint(100, 10000),
                timestamp=datetime.datetime.now().isoformat()
            )

    def fetch_market_data(self) -> List[MarketDataSchema]:
        """Return all market data as a list"""
        return list(self._market_data.values())

    def create_market_data(self, data: MarketDataSchema) -> MarketDataSchema:
        """Create or update market data for a symbol"""
        # Set timestamp if not provided
        if not data.timestamp:
            data.timestamp = datetime.datetime.now().isoformat()
        
        # Store the data
        self._market_data[data.symbol] = data
        return data

    def get_market_data_by_symbol(self, symbol: str) -> Optional[MarketDataSchema]:
        """Get market data for a specific symbol"""
        return self._market_data.get(symbol)