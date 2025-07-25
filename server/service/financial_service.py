from repository import (customer_balance,
                        search_past_financial_transactions,
                        simple_search,
                        insert_bank_transfer)
from utilities import bank_account_decode


def get_customer_balance(customer_id):

    balance_sum = customer_balance(customer_id)
    return balance_sum


def do_past_fin_transactions(customer_id, start_date, end_date):

    transfers = search_past_financial_transactions(customer_id, start_date, end_date)

    for trans in transfers.values():
        trans["bank_account"] = bank_account_decode(trans["bank_account"])

    return True, transfers


def make_bank_transfer(customer_id, to_transfer):

    to_transfer["customer_id"] = customer_id

    transaction_type = simple_search("fin_transaction_types", "fin_transaction_type", to_transfer["transfer_type"])

    to_transfer["fin_transaction_type_id"] = transaction_type["row_result0"]["fin_transaction_type_id"]

    if to_transfer["transfer_type"] == "withdrawal":
        customer_balance = get_customer_balance(customer_id)
        if to_transfer["fin_amount"] > customer_balance["actual_balance"]:
            raise ValueError("Nicht genügt Geld auf dem Konto")
    elif to_transfer["transfer_type"] != "deposit":
        raise ValueError("Fehler in der Zuordung")

    bankaccount = simple_search("financials", "customer_id", customer_id)

    to_transfer["bank_account"] = bankaccount["row_result0"]["reference_account"]

    b_transfer_id = insert_bank_transfer(to_transfer)

    financial_transfer_data = simple_search("financial_transactions", "financial_transfer_id", b_transfer_id)

    financial_transfer_data["row_result0"]["bank_account"] = bank_account_decode(
        financial_transfer_data["row_result0"]["bank_account"])
    return financial_transfer_data


if __name__ == "__main__":
    print("test")
    customer_id = 1

    start_date = "2025-01-01"
    end_date = "2025-31-06"

    answer = do_past_fin_transactions(customer_id, start_date, end_date)

    print(" ")

    print(answer)

