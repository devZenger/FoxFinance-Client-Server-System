from repository import (simple_search,
                        stock_transactions_overview,
                        search_past_transactions,
                        search_order_charges)

from utilities import date_form_validation


def customer_name(customer_id):

    table = "customers"
    condition = "customer_id"

    result = simple_search(table, condition, customer_id)
    result = result["row_result0"]
    name = f"{result["first_name"]} {result["last_name"]}"

    return name


def depot_overview(customer_id):

    return stock_transactions_overview(customer_id)


def past_transactions(customer_id, start_date, end_date):

    date_form_validation(start_date)
    date_form_validation(end_date)

    transactions = search_past_transactions(customer_id, start_date, end_date)
    for trans in transactions.values():

        volume = trans["amount"] * trans["price_per_stock"]
        order_charge = search_order_charges(volume, trans["transaction_date"])
        order_charge_total = order_charge["order_charge"] * volume
        trans["total_order_charge"] = order_charge_total

    return transactions


if __name__ == "__main__":

    start = "2025-01-12"
    end = "2025-05-13"

    answer = past_transactions(101, start, end)

    print("+ + + + + +")
    print(answer)
