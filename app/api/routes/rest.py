from fastapi import APIRouter, HTTPException
from app.schemas.market_data import MarketDataSchema
from app.services.market_data_service import MarketDataService

router = APIRouter()
market_data_service = MarketDataService()

@router.get("/market-data", response_model=list[MarketDataSchema])
async def get_market_data():
    try:
        data = market_data_service.fetch_market_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/market-data", response_model=MarketDataSchema, status_code=201)
async def create_market_data(market_data: MarketDataSchema):
    try:
        created_data = market_data_service.create_market_data(market_data)
        return created_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/market-data/{symbol}", response_model=MarketDataSchema)
async def get_market_data_by_symbol(symbol: str):
    try:
        data = market_data_service.get_market_data_by_symbol(symbol)
        if not data:
            raise HTTPException(status_code=404, detail=f"Market data for symbol {symbol} not found")
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))