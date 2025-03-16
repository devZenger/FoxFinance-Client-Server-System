import requests


from datetime import datetime, timedelta

from .server_request_depot import ServerRequestDepot




class FinancialHistory(ServerRequestDepot):

    def __init__(self, token):
        
        self.token = token
        self.status_code = None
        
        self._start_time = None
        self._end_time = None
        
        self.form_names = {"start_time":"Startdatum (jjjj-mm-tt) ",
                           "end_time":"Enddatum (jjjj-mm-tt) "}

        self.column_names = {"fin_transaction_id":"T. Nr.",
                           "fin_transaction_date":"Datum",
                           "fin_transaction_types":"Art der T.",
                           "fin_amount":"Betrag",
                           "bank_account":"Bankkonto"}

        super().__init__()
    
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, input:str):
        print(f"input = {input}")
        split = input.split("-")
        print(f"split= {len(split[0])}    split= {split[0]}")
        if len(split[0]) == 4 and len(split[1])==2 and len(split[2])==2:
            print(f"start time. {input}")
            self._start_time=input
        else:
            raise ValueError("Eingabeformat muss yyyy-mm-dd entsprechen")

    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, input:str):
        split = input.split("-")

        if len(split[0]) == 4 and len(split[1])==2 and len(split[2])==2:
            print(f"end_time = {input}")
            self._end_time=input
        else:
            raise ValueError("Eingabeformat muss yyyy-mm-dd entsprechen")
    
    
    

    def get_actual_balance(self):
        
        url_part = 'current_balance/'
        
        status, self.response = self.get_without_parameters(url_part)
        print(f"get-acutal_balance: self.response: {self.response}")
        
        if status:
            1
            self.response["Aktueller Kontostand: "]=self.response.pop("actual_balance")
    
        
        return status



    def get_financial_transaction_by_timespan(self):
        
        url_part = 'pastfinancialtransactions/'
        
        status, self.response = self.get_with_parameters(url_part, self.start_time, self.end_time)
        
        return status

    
    
    def get_last_three_months(self):
        
        today =datetime.today()
        three_months_ago = today - timedelta(days=90)

        self.end_time =today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")
        
        result = self.get_financial_transaction_by_timespan()
        
        return result

    def get_last_twelve_months(self):
        
        today =datetime.today()
        three_months_ago = today - timedelta(days=365)

        self.end_time =today.strftime("%Y-%m-%d")
        self.start_time = three_months_ago.strftime("%Y-%m-%d")
        
        result = self.get_financial_transaction_by_timespan()
        
        return result
    
    

        
        
        
        
