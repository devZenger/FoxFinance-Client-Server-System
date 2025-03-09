from repository import simple_search, latest_trade_day_entry, trade_day_by_period


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
    
    #presenable_data = performance_data_presentable(performance_data)
    
    return performance_data
    
        



def performance_data_presentable(performance_data):
    
    data_presentable = {}
    
    data_presentable["name"]= f'\tName: {performance_data["stocks_row"]["company_name"]}'
    data_presentable["symbol"]=f"\tSymbol: {performance_data["stocks_row"]["ticker_symbol"]}"
    data_presentable["isin"]=f"\tISIN: {performance_data["stocks_row"]["isin"]}"
    
    data_presentable["trade_day"]=f"\tAktuellster Handelstag: {performance_data["latest_day"]["date"]}"
    data_presentable["open"]=f"\tÖffnungskurs:\t {performance_data["latest_day"]["open"]:.2f} €"
    data_presentable["high"]=f"\thöchster Kurs:\t {performance_data["latest_day"]["high"]:.2f} €"
    data_presentable["low"]=f"\ttiefster Kurs:\t {performance_data["latest_day"]["low"]:.2f} €"
    data_presentable["close"]=f"\tSchlusskurs:\t {performance_data["latest_day"]["close"]:.2f} €"

    data_presentable["time0"]="\tPerformance über 6 Monate: "
    data_presentable["price0"]=f"\tKurs:\t\t {performance_data["6 months"]["price"]:.2f} €"
    data_presentable["perform0"]=f"\tVeränderung:\t {performance_data["6 months"]["performance"]:.2f}%"
 
    data_presentable["time1"]="\tPerformance über ein Jahr: "
    data_presentable["price1"]=f"\tKurs:\t\t {performance_data["1 years"]["price"]:.2f} €"
    data_presentable["perform1"]=f"\tVeränderung:\t {performance_data["1 years"]["performance"]:.2f}%"

    data_presentable["time2"]="\tPerformance über 6 Monate: "
    data_presentable["price2"]=f"\tKurs:\t\t {performance_data["2 years"]["price"]:.2f} €"
    data_presentable["perfom2"]=f"\tVeränderung:\t {performance_data["2 years"]["performance"]:.2f}%"
    
    return data_presentable
    
    
    
    
if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "isin"
    search_term = "DE0005190003"
    time = "6 months"
    
    performance_data = search_stock(search_term)
    
    print(performance_data)
    print(performance_data)
    #for an in answer:
    #    print(an)

    for per in performance_data.values():
        print(per)



    #print(len(answer))
    line = "-"*80
    print(" ")
    test= """ print("\tName: ", performance_data["stocks_row"]["company_name"])
    print("\tSymbol: ", performance_data["stocks_row"]["ticker_symbol"])
    print("\tISIN: ", performance_data["stocks_row"]["isin"])
    print(line)
    print("\tAktuellster Handelstag:", performance_data["latest_day"]["date"])
    print(f"\tÖffnungskurs:\t {performance_data["latest_day"]["open"]:.2f} €")
    print(f"\thöchster Kurs:\t {performance_data["latest_day"]["high"]:.2f} €")
    print(f"\ttiefster Kurs:\t {performance_data["latest_day"]["low"]:.2f} €")
    print(f"\tSchlusskurs:\t {performance_data["latest_day"]["close"]:.2f} €")
    print(line)
    print("\tPerformance über 6 Monate: ")
    print(f"\tKurs:\t\t {performance_data["6 months"]["price"]:.2f} €")
    print(f"\tVeränderung:\t {performance_data["6 months"]["performance"]:.2f}%")
    print(line)
    print("\tPerformance über ein Jahr: ")
    print(f"\tKurs:\t\t {performance_data["1 years"]["price"]:.2f} €")
    print(f"\tVeränderung:\t {performance_data["1 years"]["performance"]:.2f}%")
    print(line)
    print("\tPerformance über 6 Monate: ")
    print(f"\tKurs:\t\t {performance_data["2 years"]["price"]:.2f} €")
    print(f"\tVeränderung:\t {performance_data["2 years"]["performance"]:.2f}%")
    print(line)
 """
    #stocks_row = answer["row_result0"]
    #print(stocks_row) 

    
    
    
    
    
    
    
    
            
            
    
    
