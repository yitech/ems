from fastapi import APIRouter, HTTPException
from app.schemas.market_data import MarketDataResponse
from app.services.market_data_service import MarketDataService

router = APIRouter()
service = MarketDataService()

@router.get("/market-data/{symbol}", response_model=MarketDataResponse)
async def get_market_data(symbol: str):
    data = await service.fetch_market_data(symbol)
    if data is None:
        raise HTTPException(status_code=404, detail="Market data not found")
    return data

@router.post("/market-data/", response_model=MarketDataResponse)
async def create_market_data(market_data: MarketDataResponse):
    created_data = await service.create_market_data(market_data)
    return created_data