from repository import (customer_balance,
                        search_past_financial_transactions,
                        simple_search,
                        insert_bank_transfer)
from schemas import BankTransfer

from .utility import date_form_validation
from utilitys import bank_account_decode


def get_customer_balance(customer_id):

    try:
        balance_sum = customer_balance(customer_id)

        return balance_sum

    except Exception as e:
        print(f"get_customer_balance Error: {e}")
        raise ValueError(e)


def do_past_fin_transactions(customer_id, start_date, end_date):

    try:
        date_form_validation(start_date)
        date_form_validation(end_date)
        transfers = search_past_financial_transactions(customer_id,
                                                       start_date,
                                                       end_date)

        for trans in transfers.values():
            trans["bank_account"] = bank_account_decode(trans["bank_account"])

        return transfers

    except Exception as e:
        raise ValueError(e)


def make_bank_transfer(customer_id, bank_transfer: BankTransfer):

    transfer_dic = {}
    transfer_dic["customer_id"] = customer_id
    transfer_dic["fin_amount"] = bank_transfer.fin_amount
    transfer_dic["usage"] = bank_transfer.usage

    try:
        transaction_type = simple_search("fin_transaction_types",
                                         "fin_transaction_type",
                                         bank_transfer.transfer_type)

        transfer_dic["fin_transaction_type_id"] = transaction_type["row_result0"]["fin_transaction_type_id"]

        if bank_transfer.transfer_type == "withdrawal":
            customer_balance = get_customer_balance(customer_id)
            if transfer_dic["fin_amount"] > customer_balance["actual_balance"]:
                raise ValueError("Nicht genügt Geld auf dem Konto")
        elif bank_transfer.transfer_type != "deposit":
            raise ValueError("Fehler in der Zuordung")

        bankaccount = simple_search("financials", "customer_id", customer_id)

        transfer_dic["bank_account"] = bankaccount["row_result0"]["reference_account"]

        b_transfer_id = insert_bank_transfer(transfer_dic)

        financial_transfer_data = simple_search("financial_transactions",
                                                "financial_transfer_id",
                                                b_transfer_id)

        financial_transfer_data["row_result0"]["bank_account"] = bank_account_decode(financial_transfer_data["row_result0"]["bank_account"])
        return financial_transfer_data

    except Exception as e:
        print(f"make_bank_transfer: {e}")
        raise ValueError(f"at make bank transfer, Error: {e}")


if __name__ == "__main__":
    print("test")
    customer_id = 1

    transfer = BankTransfer(
        fin_amount=100.0,
        transfer_type="withdrawal",
        usage="Test")

    start_date = "2025-01-01"
    end_date = "2025-31-06"

    answer = do_past_fin_transactions(customer_id, start_date, end_date)

    print(" ")

    print(answer)

    print(" ")
    stocks_row = answer["row_result0"]
    print(stocks_row)
