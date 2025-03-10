from typing import Annotated

from fastapi import Depends,APIRouter
from pydantic import BaseModel


from service import User, get_current_active_user, search_stock, buy_stocks, sell_stocks

router = APIRouter()

class User(BaseModel):
    #username: str
    email: str 
    customer_id: int | None = None
    disabled: bool | None = None

class StockTrade(BaseModel):
    isin: str
    count: int
    transaction_type: str
    



@router.get("/depot/stocksearch/{search_term}")
async def get_stock_search(search_term:str, current_customer: Annotated[User, Depends(get_current_active_user)]):
     
    result = search_stock(search_term)     
    return {"message":result}


@router.post("/depot/tradestocks/")
async def trade_stocks(stock_trade: StockTrade, current_customer: Annotated[User, Depends(get_current_active_user)]):
    
    
    
    if stock_trade.transaction_type == "buy":
     
        validation = buy_stocks(current_customer["customer_id"], stock_trade)
        
        return {"message": validation}
    
    elif stock_trade.transaction_type == "sell":
        
        validation = sell_stocks(current_customer["customer_id"], stock_trade)
    
    else:
        return {"message": "Konnte Anfrage ich ausführen"}
        
    
    
    
    