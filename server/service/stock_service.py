from datetime import date, datetime, timedelta

from repository import (simple_search,
                        latest_trade_day_entry,
                        trade_day_by_period,
                        search_order_charges,
                        all_stocks_by_customer,
                        customer_balance,
                        insert_stock_transaction,
                        update_single_stock_datas)
from schemas import StockTrade


def search_stock(search_input):

    search_term = f"%{search_input}%"
    table = "stocks"

    result = simple_search(table, "company_name", search_term)

    if result == {}:
        result = simple_search(table, "ticker_symbol", search_term)
        if result == {}:
            result = simple_search(table, "isin", search_term)

    if result == {}:
        return "Die Aktien konnte nicht gefunden werden"

    elif len(result) > 1:
        return result

    else:
        end_result = {}
        stocks_row = result["row_result0"]
        performance_data = stock_performence(stocks_row)
        end_result["one"] = performance_data.copy()

        return end_result


def stock_performence(stocks_row: dict):

    isin = stocks_row["isin"]

    update_single_stock_datas(isin)

    last_trade_day = latest_trade_day_entry(isin)

    timespan = ["6 months", "1 years", "2 years"]

    performance_data = {}

    for time in timespan:

        if time == "6 months":
            time_dif = timedelta(days=(183))
        elif time == "1 years":
            time_dif = timedelta(days=365)
        elif time == "2 years":
            time_dif = timedelta(days=730)
        else:
            raise ValueError("Zeitspanne konnte nicht zugeordnet werden.")

        search_date = (datetime.now()-time_dif).date()

        result = trade_day_by_period(isin, search_date)

        performance = result["open"]/last_trade_day["close"] * 100
        data = {}
        data["date"] = result["date"]
        data["price"] = result["open"]
        data["performance"] = performance

        performance_data[f"{time}"] = data.copy()

    performance_data["stocks_row"] = stocks_row.copy()
    performance_data["latest_day"] = last_trade_day.copy()

    return performance_data


# prepare for database
def stocks_trade(customer_id, stock_trade: StockTrade):

    update_single_stock_datas(stock_trade.isin)

    current_market = latest_trade_day_entry(stock_trade.isin)
    trade_vol = current_market["close"] * stock_trade.amount

    current_day = date.today()

    current_charges = search_order_charges(trade_vol, current_day)

    trade_charge = trade_vol * current_charges["order_charge"]

    if (stock_trade.transaction_type != "buy" and
            stock_trade.transaction_type != "sell"):
        raise ValueError("transaction_type is wrong")

    transaction = {
            "customer_id": customer_id,
            "isin": stock_trade.isin,
            "transaction_type": stock_trade.transaction_type,
            "amount": stock_trade.amount,
            "price_per_stock": current_market["close"],
            "order_charge_id": current_charges["order_charge_id"]
        }

    return transaction, trade_charge, trade_vol


def customer_finance_data(customer_id, kind_of):

    customer_finance = customer_balance(customer_id)

    account = simple_search("financials", "customer_id", customer_id)

    fin_transaction_type = simple_search("fin_transaction_types",
                                         "fin_transaction_type",
                                         kind_of)
    bts_id = fin_transaction_type["row_result0"]["fin_transaction_type_id"]

    bank_account = account["row_result0"]["reference_account"]

    balance = {
            "customer_id": customer_id,
            "bank_account": bank_account,
            "fin_transaction_type_id": bts_id
        }

    return customer_finance, balance


def buy_stocks(customer_id, stock_trade: StockTrade):

    transaction, trade_charge, trade_vol = stocks_trade(customer_id, stock_trade)

    customer_finance, balance = customer_finance_data(customer_id, "buy stocks")

    total = trade_vol+trade_charge

    if customer_finance["actual_balance"] < total:

        return ("Guthaben reicht nicht aus")

    else:
        balance["fin_amount"] = total

        return trade_transaction(transaction, balance)


# input in database
def trade_transaction(transaction: dict, balance: dict):

    validation = {}

    try:
        transaction_id, balance_id = insert_stock_transaction(transaction,
                                                              balance)

        transaction_insert = simple_search("transactions", "transaction_id",
                                           transaction_id)
        balance_insert = simple_search("financial_transactions",
                                       "financial_transfer_id",
                                       balance_id)

        validation["stock_trade"] = transaction_insert["row_result0"]
        validation["balance_statement"] = balance_insert["row_result0"]

    except Exception as e:
        validation["error"] = f"Transaktion konnte nicht ausgeführt werden: {e}"

    finally:
        return validation


def sell_stocks(customer_id, stock_trade: StockTrade):

    ownership = all_stocks_by_customer(customer_id, stock_trade.isin)

    if stock_trade.amount > ownership:

        return "Nicht genügend Aktien"

    else:

        transaction, trade_charge, trade_vol = stocks_trade(customer_id, stock_trade)

        customer_finance, balance = customer_finance_data(customer_id, "sell stocks")

        balance["fin_amount"] = (trade_vol - trade_charge)

        return trade_transaction(transaction, balance)


def start_stock_transaction(customer_id, stock_trade: StockTrade):

    try:
        if stock_trade.transaction_type == "buy":

            validation = buy_stocks(customer_id, stock_trade)

            return validation

        elif stock_trade.transaction_type == "sell":

            validation = sell_stocks(customer_id, stock_trade)

            return validation

        else:
            raise ValueError("Anfrage muss buy oder sell enthalten")

    except Exception as e:
        print(f"Error at start_stock_transaction, Error: {e}\n")
        raise Exception(e)
