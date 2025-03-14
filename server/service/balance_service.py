from pydantic import BaseModel
from decimal import Decimal

from repository import customer_balance, search_past_balance_transactions, simple_search, insert_balance_transaction

from .utility import date_form_validation

class CashTransfer(BaseModel):
    balance_sum: Decimal
    transaction_type: str
    usage: str | None = None


def get_customer_balance(customer_id):
    
    try:
        balance_sum = customer_balance(customer_id)

        return balance_sum
    
    except Exception as e:
        print(f"get_customer_balance Error: {e}")
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
    transfer_dic["balance_sum"]= cash_transfer.balance_sum
    transfer_dic["usage"]= cash_transfer.usage
    
    try:
        type_of_action = simple_search("balance_transactions_type", "type_of_action", cash_transfer.transaction_type)
        
        transfer_dic["balance_transaction_type_id"] = type_of_action["row_result0"]["balance_transaction_type_id"]
        
        if cash_transfer.transaction_type == "withdrawal":
            customer_balance = get_customer_balance(customer_id)
            if cash_transfer.balance_sum > customer_balance["actual_balance"]:
                raise ValueError("Nicht genügt Geld auf dem Konto")
        elif cash_transfer.transaction_type != "deposit":
            raise ValueError("Fehler in der Zuordung")
        
        bankaccount = simple_search("financials", "customer_id", customer_id)
        
        transfer_dic["bank_account"]= bankaccount["row_result0"]["reference_account"]
        
        b_transaction_id = insert_balance_transaction(transfer_dic)
        
        balance_transaction_data = simple_search("balance_transactions", "balance_transaction_id", b_transaction_id)
        
        return balance_transaction_data

    except Exception as e:
        print(f"make_balance_transaction: {e}")
        raise ValueError(e)

    


if __name__ == "__main__":

    customer_id = 1
    
    transfer = CashTransfer(
        balance_sum = Decimal(3400.00),
        transaction_type = "withdrawal",
        usage="Test")
    
    print(transfer)
    
    answer = make_balance_transaction(customer_id, transfer)
    
    print(" ")

    print(answer)
    
    print(" ")
    stocks_row = answer["row_result0"]
    print(stocks_row)