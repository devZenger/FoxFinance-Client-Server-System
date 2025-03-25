from pydantic import BaseModel

from datetime import date

from repository import simple_search, latest_trade_day_entry, trade_day_by_period, search_order_charges, all_stocks_by_customer, customer_balance, insert_stock_transaction


class StockTrade(BaseModel):
    isin: str
    amount: int
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
        
        return result1


def stock_performence(stocks_row:dict):
 
    isin = stocks_row["isin"]
    print(f"isin ist = {isin}")
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
        
    
    performance_data["stocks_row"]=stocks_row.copy()
    performance_data["latest_day"]=last_trade_day.copy()

    
    return performance_data
    
    #prepare for database
def stocks_trade(customer_id, stock_trade:StockTrade):
    
    current_market = latest_trade_day_entry(stock_trade.isin)  
    trade_vol = current_market["close"]* stock_trade.amount
    
    current_day= date.today()
    
    current_charges = search_order_charges(trade_vol, current_day)
    
    trade_charge = trade_vol * current_charges["order_charge"]

    if stock_trade.transaction_type != "buy" and stock_trade.transaction_type != "sell":
        raise ValueError("transaction_type is wrong")

    transaction = {
            "customer_id":customer_id,
            "isin": stock_trade.isin,
            "transaction_type": stock_trade.transaction_type,
            "amount":stock_trade.amount,
            "price_per_stock":current_market["close"],
            "order_charge_id":current_charges["order_charge_id"]    
        }

    return transaction, trade_charge, trade_vol#, customer_finance, balance


def customer_finance_data(customer_id, kind_of):
    
    customer_finance = customer_balance(customer_id)
    
    account = simple_search("financials","customer_id", customer_id)
    
    
    fin_transaction_type = simple_search("fin_transaction_types", "fin_transaction_type",kind_of)
    bts_id = fin_transaction_type["row_result0"]["fin_transaction_type_id"]
    print("bts_id:", bts_id)
    print(f"balance: {account}")
    
    bank_account = account["row_result0"]["reference_account"]
    
    balance = {
            "customer_id":customer_id,
            "bank_account": bank_account,
            "fin_transaction_type_id": bts_id
        }
    
    return customer_finance, balance

 
def buy_stocks(customer_id, stock_trade:StockTrade):
    
    transaction, trade_charge, trade_vol = stocks_trade(customer_id, stock_trade)
    
    customer_finance, balance =customer_finance_data(customer_id, "buy stocks")
        
    total = trade_vol+trade_charge
    
    print(f"customer finance: {customer_finance}")
    
    print(f"customer blanance: {customer_finance["actual_balance"]}")
    print(f"total = {total}")
    
    if customer_finance["actual_balance"] < total:
        print("Guthaben reicht nicht aus")
        return ("Guthaben reicht nicht aus")
    
    else:

        print("Guthaben reicht aus")


        balance["fin_amount"]=total
        
        return trade_transaction(transaction, balance)


    #input in database
def trade_transaction(transaction:dict, balance:dict):
    
    print("start trade_transaction")
    
    validation={}

    try: 
        transaction_id, balance_id = insert_stock_transaction(transaction, balance)
        
        print("report anfrage")
        
        transaction_insert = simple_search("transactions","transaction_id", transaction_id)
        balance_insert = simple_search("financial_transactions","financial_transfer_id", balance_id)
        
        validation["stock_trade"] = transaction_insert["row_result0"]
        validation["balance_statement"] = balance_insert["row_result0"]
    
    except Exception as e:
        validation["error"] = f"Transaktion konnte nicht ausgeführt werden: {e}"
        
    
    finally:
        return validation


def sell_stocks(customer_id, stock_trade:StockTrade):
    
    ownership = all_stocks_by_customer(customer_id, stock_trade.isin)
    
    if stock_trade.amount > ownership:
        
        return "Nicht genügend Aktien"
    
    else:
        
        transaction, trade_charge, trade_vol = stocks_trade(customer_id, stock_trade)
        
        customer_finance, balance =customer_finance_data(customer_id, "sell stocks")
        
        balance["fin_amount"]= (trade_vol - trade_charge)
        
        
        return trade_transaction(transaction, balance)


def start_stock_transaction(customer_id, stock_trade:StockTrade):
    
    try:
        if stock_trade.transaction_type == "buy":
     
            validation = buy_stocks(customer_id, stock_trade)

            return validation
    
        elif stock_trade.transaction_type == "sell":
        
            validation = sell_stocks(customer_id, stock_trade)
            
            return validation
    
        else:
            raise ValueError("Anfrage muss buy oder sell enthalten")

    except Exception as e:
        print(f"Error at start_stock_transaction, Error: {e}\n")
        raise Exception(e)






    

    
if __name__ == "__main__":
    
    from pydantic import BaseModel

    class StockTrade(BaseModel):
        isin: str
        amount: int
        transaction_type: str
    
    
    stock_trade = StockTrade(isin = "DE0005190003", amount=10, transaction_type="sell")
    
    
    print("start")
    table = "stocks"
    column = "isin"
    search_term = "DE0005190003"
    time = "6 months"
    
    performance_data = buy_stocks(1, stock_trade)


    print("--------------------------")    
    print(performance_data)

    print("---------------------------")


    
    
    
    
    
    
    
    
            
            
    
    
