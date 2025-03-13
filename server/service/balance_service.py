from pydantic import BaseModel
from decimal import Decimal

from repository import customer_balance, search_past_balance_transactions, simple_search, insert_balance_transaction

from .utility import date_form_validation

class CashTransfer(BaseModel):
    balance_sum: Decimal
    transaction_type: str


def get_customer_balance(customer_id):
    
    try:
        balance_sum = customer_balance(customer_id)
        
        return balance_sum
    
    except Exception as e:
        raise ValueError(e)
    

def get_past_balance_transactions(customer_id, start_date, end_date):
    
    try:
        
        date_form_validation(start_date)
        date_form_validation(end_date)
        
        transactions = search_past_balance_transactions(customer_id, start_date, end_date)

        return transactions
        
    except Exception as e:
        raise ValueError(e)




    
    

def make_balance_transaction(customer_id, cash_transfer:CashTransfer):
    
    transfer_dic={}
    
    transfer_dic["customer_id"]= customer_id
    transfer_dic["balance_sum"]= cash_transfer.sum
    
    try:
        
        type_of_action = simple_search("balance_transactions_type", "type_of_action", cash_transfer.transaction_type)
        transfer_dic["balance_transactions_type_id"] = type_of_action["balance_transactions_type_id"]
        
        if cash_transfer.transaction_type == "withdraw":
            if cash_transfer.balance_sum > get_customer_balance(customer_id):
                raise ValueError("Nicht genügt Geld auf dem Konto")
        
        b_transaction_id = insert_balance_transaction(transfer_dic)
        
        balance_transaction_data = simple_search("balance_transactions", "balance_transaction_id", b_transaction_id)
        
        return balance_transaction_data
        
        
        
     
     
    except Exception as e:
        raise ValueError(e)

    
