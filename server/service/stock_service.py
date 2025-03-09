from pydantic import BaseModel

from datetime import date

from repository import simple_search, latest_trade_day_entry, trade_day_by_period, search_order_charges, insert_one_table


class StockTrade(BaseModel):
    isin: str
    count: int
    transaction_type: str


def search_stock(search_input):
    
    search_term = f"%{search_input}%"
    table = "stocks"
    
    
    result = simple_search(table, "company_name", search_term)
    
    if result== {}:    
        result = simple_search(table, "ticker_symbol", search_term)
        if result == {}:
            result = simple_search(table, "isin", search_term)
    
    print(result)
    print(len(result))
    
    if result == {}:
        return "Die Aktien konnte nicht gefunden werden"
    
    elif len(result) >1:
        return result
    
    else:
        result1 = {}
        stocks_row = result["row_result0"]
        performance_data = stock_performence(stocks_row)
        result1["one"] = performance_data.copy()
        #presenable_data = performance_data_presentable(performance_data)
        
        return result1


def stock_performence(stocks_row:dict):
 
    isin = stocks_row["isin"]
    
    print(f"stocks_row {stocks_row}")
    
    last_trade_day = latest_trade_day_entry(isin)
    
    print(last_trade_day)
    
    
    timespan = ["6 months", "1 years", "2 years"] #, "3 years"]
    
    performance_data = {}
    
    for time in timespan:
   
        result = trade_day_by_period(isin, time)
 
        performance = result["open"]/last_trade_day["close"] *100
        data = {}
        data["date"]= result["date"]
        data["price"]=result["open"]
        data["performance"]=performance
 
        performance_data[f"{time}"]=data.copy()
        
        print("++++++++")
        print(performance_data) 
        print("-------------")   
    
    
    print(performance_data)
    
    performance_data["stocks_row"]=stocks_row.copy()
    performance_data["latest_day"]=last_trade_day.copy()

    
    return performance_data
    
 
 
def buy_stocks(customer_id, stock_trade:StockTrade): 
        
    current_market = latest_trade_day_entry(stock_trade.isin)  
     
    trade_vol = current_market["close"]* stock_trade.count
    
    current_day= date.today()
    
    print(current_day)
    
    current_charges = search_order_charges(trade_vol, current_day)
    
    trade_charge = trade_vol * current_charges["order_charge"]
    
    
    
    customer_finance_result = simple_search("financials", "customer_id",  customer_id)
    
    customer_finance = customer_finance_result["row_result0"]
        
    
    total = trade_vol+trade_charge
    
    print(customer_finance)
    
    if customer_finance["balance"] < total:
        
        return ("Guthaben reicht nicht aus")
    
    else:
        
        transaction_type = simple_search("transaction_type", "kind_of_action","buy")
        print(transaction_type)
        ts_id = transaction_type["row_result0"]["transaction_type_id"]
        
        transaction = {
            "customer_id":customer_id,
            "isin": stock_trade.isin,
            "transaction_type_id": ts_id,
            "count":stock_trade.count,
            "price_per_stock":current_market["close"],
            "order_charge_id":current_charges["order_charge_id"]    
        }
        
        balance_transaction_type = simple_search("balance_transactions_type", "type_of_action","buy stocks")
        print("balance", balance_transaction_type)
        bts_id = balance_transaction_type["row_result0"]["balance_transaction_type_id"]
        
        
        balance = {
            "customer_id":customer_id,
            "bank_account":customer_finance["reference_account"],
            "balance_sum": total,
            "balance_transaction_type_id": bts_id
        }
        
        return trade_transaction(transaction, balance)


def trade_transaction(transaction:dict, balance:dict):
    
    try:
        transaction_id = insert_one_table("transactions", transaction)
        balance["usage"]= f"Aktientransaktions Nr.: {transaction_id}"
        
        
        transaction_insert = simple_search("transactions","transaction_id", transaction_id)
        
        
        
        
        balance_id = insert_one_table("balance_transactions", balance)
        
        balance_insert = simple_search("balance_transactions","balance_transaction_id", balance_id)
        
        validation={}
        validation["stock_trade"] = transaction_insert["row_result0"]
        validation["balance_statement"] = balance_insert["row_result0"]
                                              
        
        return validation
    
    except Exception as e:
        return e
        
        
    
    
    
    
    
    
    
if __name__ == "__main__":
    
    from pydantic import BaseModel

    class StockTrade(BaseModel):
        isin: str
        count: int
        transaction_type: str
    
    
    stock_trade = StockTrade(isin = "DE0005190003", count=20, transaction_type="buy")
    
    
    print("start")
    table = "stocks"
    column = "isin"
    search_term = "DE0005190003"
    time = "6 months"
    
    performance_data = buy_stocks(2, stock_trade)


    print("--------------------------")    
    print(performance_data)

    print("---------------------------")


    
    
    
    
    
    
    
    
            
            
    
    
