from repository import customer_balance, search_past_balance_transactions

from .utility import date_form_validation

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
