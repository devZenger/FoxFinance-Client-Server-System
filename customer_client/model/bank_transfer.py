from decimal import Decimal

from .server_request_depot import ServerRequestDepot

from .financial_history import FinancialHistory

class BankTransfer(ServerRequestDepot):
    def __init__(self, token):
        
        self.token = token
        
        self._fin_amount = None
        self._transaction_type = None
        self._usage = None
     
        self.form_names = {"fin_amount":"Betrag (. statt ,) ",
                            "transaction_type":"Einzahlen oder Auszahlen ",
                            "usage":"Verwendungszweck "}
        
        super().__init__()
    
    @property
    def fin_amount(self):
        return self._fin_amount
    
    @fin_amount.setter
    def fin_amount(self, input:str):
        if "," in input:
            input = input.replace("",","".")
        input = float(input) 
        
        print(f"input= {input}")
            
        if input >= 0:
            self._fin_amount = input
        else:
            raise ValueError("Mindestens 1 Cent")
    
    
    @property
    def transaction_type(self):
        return self._transaction_type
    
    @transaction_type.setter
    def transaction_type(self, input:str):
        
        input = input.lower()
        
        if input == "einzahlen" or input == "deposit":
            self._transaction_type = "deposit"
        elif input == "auszahlen" or input == "withdrawal":
            self._transaction_type = "withdrawal"
        else:
            raise ValueError("Fehlerhafte Eingabe")

    
    @property
    def usage(self):
        return self._usage
    
    @usage.setter
    def usage(self, input):
        
        self._usage = input


    def actual_balance(self):
        balance = FinancialHistory(self.token)
        actual_balance = balance.get_actual_balance()
        del balance
        return actual_balance


    
    def make_transfer(self):
        url_part = 'banktransfer/'
        
        to_transmit = {"fin_amount":self.fin_amount,
                       "transfer_type":self.transaction_type,
                       "usage":self.usage}
        
        return self.make_post_request(url_part, to_transmit)
        
        
    
    
        
    