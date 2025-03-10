import requests

from .url import url_server


def performance_data_presentable(performance_data):
    
    data_presentable = {}
    
    data_presentable["name"]= f'Name: {performance_data["stocks_row"]["company_name"]}'
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

    data_presentable["time2"]="\tPerformance über zwei Jahre: "
    data_presentable["price2"]=f"\tKurs:\t\t {performance_data["2 years"]["price"]:.2f} €"
    data_presentable["perfom2"]=f"\tVeränderung:\t {performance_data["2 years"]["performance"]:.2f}%"
    
    return data_presentable


class StockActions:
    def __init__(self, token):
        
        self.token=token
        
        self.search_term=None
   
        self.isin=None
        self.stock_name=None
        self.count=None
        self._type_of_action=None
        
        
        self.stock_list=None
        self.stock_information=None
        
        self.response = None
        
        self.search_form_names = {"search_term":"ISIN, Symbol oder Name eingeben: "}
        
        self.trade_form_names = {"count":"Anzahl eingeben: ", "type_of_action":"Kaufen oder Verkaufen?: "}
        
        self.make_trade_form ={"make_trade":"Handel abschließen (Ja/Nein) eingeben: "}
        
        self.form_names = {"stock_name": "Unternehmen: ", 
                           "isin": "ISIN: ", 
                           "count": "Anzahl: ",
                           "type_of_action: ": "Kaufen oder Verkaufen: "}
    
    
    @property
    def type_of_action(self):
        return self._type_of_action
    
    @type_of_action.setter
    def type_of_action(self, input:str):
        input = input.lower()
        if input == "kaufen" or input == "verkaufen":
            self._email = input
        else:
            raise ValueError("Fehler")
    
    @property
    def make_trade(self):
        return self._make_trade
    
    @make_trade.setter
    def make_trade(self, input:str):
        input = input.lower()
        if input == "ja" or input == "yes" or input == "j":
            self._make_trade = True
        elif input == "nein" or input == "no" or input == "n":
            self._make_trade = False
        else:
            raise ValueError("Fehler")
    
    
    
    
    
    def stock_search(self):
        
        get_data = self.request_server()
        
        if get_data == False:
            return f"\tFehler, {self.response.status_code}\n\tÜberprüfen Sie die Verbindung"
        else:
            results = {}
            results = self.response["message"]       
        
            if len(results) > 1:      
                result_str = "ISIN\t\t | Ticker Symbol | Firmenname\n"
                
                for result in results.values():
                
                    result_str=f"{result_str}\t"
                    for value in result.values():
                        if len(value) < 4:
                            add = "\t"
                        else:
                            add = ""
                            
                        result_str = f"{result_str}{value}{add}\t | "
                    
                    
                    result_str= result_str[:-2]
                    result_str= f"{result_str}\n"
                
                self.stock_list = f"{result_str}\n\tEs wurden mehrere gefunden"

            
            
                return "several_stocks"  

            else:
                
                self.isin = results["one"]["latest_day"]["isin"]
                self.stock_name = results["one"]["stocks_row"]["company_name"]
                
                print(f"self.isin = {self.isin}")
                
                presantable = performance_data_presentable(results["one"])
                
                self.stock_information= ""
                
                for pre in presantable.values():
                    self.stock_information=f"{self.stock_information} {pre}\n"
                
                
                
                self.stock_information=f"""{self.stock_information}\n
                \tSollte die Börse geöffnet sein,\n\tist der Schlusskurs der aktuelle Kurs"""
                
                return "single_stock"
            
        
    def request_server(self):
        
        url = f'{url_server}/depot/stocksearch/{self.search_term}'
        
        headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        self.response = requests.get(url, headers=headers)
        
        
        
        if self.response.status_code == 200:
            print ("Empfangen:", self.response.json())
            print("suche erfolgreich")
            self.response = self.response.json()
            return True
            
         
        else:
            print("Fehler", self.response.status_code)
            return False
    
    
    

        
        
    
    
    def stock_trade(self):
        
     pass
        
       
        

        
    
