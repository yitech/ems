from pydantic import BaseModel
from typing import List, Optional

class MarketData(BaseModel):
    symbol: str
    price: float
    volume: int
    timestamp: str

class MarketDataResponse(BaseModel):
    data: List[MarketData]
    message: Optional[str] = None
    error: Optional[str] = None