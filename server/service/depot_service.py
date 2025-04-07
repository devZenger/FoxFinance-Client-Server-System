from repository import stock_transactions_overview, search_past_transactions

from .utility import date_form_validation


def depot_overview(customer_id):

    return stock_transactions_overview(customer_id)


def past_transactions(customer_id, start_date, end_date):

    date_form_validation(start_date)
    date_form_validation(end_date)
    print(f"start date: {start_date}")
    transactions = search_past_transactions(customer_id,
                                            start_date,
                                            end_date)

    return transactions
