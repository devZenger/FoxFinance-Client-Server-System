from repository import stock_transactions_overview, search_past_transactions

from .utility import date_form_validation

def depot_overview(customer_id):
    
    try:
        return stock_transactions_overview(customer_id)
    
    except Exception as e:
        raise ValueError(e)
    

def past_transactions(customer_id, start_date, end_date):
    
    
    try:
        
        date_form_validation(start_date)
        date_form_validation(end_date)
        
        transactions = search_past_transactions(customer_id, start_date, end_date)

        return transactions
        
    except Exception as e:
        raise ValueError(e)


        
        





