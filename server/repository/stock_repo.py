import yfinance as yf

from utilities import (DBOperationError,
                       SQLExecutionError,
                       make_dictionary_one_result,
                       error_forwarding_msg)

# db_op - Instanz von DBOperator
from .db_operator import db_op
from .search_repo import simple_search


def latest_trade_day_entry(search_term):

    try:
        db_op.open_connection_db()

        sql = """SELECT *
                 FROM stock_data
                 WHERE isin = ?
                 ORDER BY date DESC LIMIT 1"""

        value = (search_term,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        result = make_dictionary_one_result(datas[0], names)

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except Exception as e:
        error = f"Fehler bei latest_trade_day_entry(" \
                f"search_term: {search_term})" \
                f".\nError: {e}\n"
        print(error)
        result = f"Kein Eintrag gefunden, Error: {e}"

    finally:
        db_op.close()
        return result


def trade_day_by_period(search_term, time):

    try:
        db_op.open_connection_db()

        sql = """SELECT *
                 FROM stock_data
                 WHERE isin = ? AND date <= ?
                 ORDER BY date DESC LIMIT 1"""

        value = (search_term, time)
        datas = db_op.execute(sql, value).fetchall()
        names = db_op.col_names()

        result = make_dictionary_one_result(datas[0], names)

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except SQLExecutionError as e:
        error = f"Fehler bei trade_day_by_period(" \
                f"search_term: {search_term}, time: {time}).\nError: {e}\n"
        print(error)
        result = f"Kein Eintrag gefunden, Error: {e}"

    finally:
        db_op.close()
        return result


def all_stocks_by_customer(customer_id, isin):

    try:
        db_op.open_connection_db()

        sql = """SELECT
                    COALESCE((SELECT SUM(amount)
                        FROM transactions
                        WHERE customer_id = ?
                            AND isin = ?
                            AND transaction_type = 'buy'), 0) -
                    COALESCE((SELECT SUM(amount)
                        FROM transactions
                        WHERE customer_id = ?
                            AND isin = ?
                            AND transaction_type = 'sell'), 0)
                AS DIFFERENCE"""

        value = (customer_id, isin, customer_id, isin,)
        datas = db_op.execute(sql, value).fetchall()

        result = datas[0][0]

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except Exception as e:
        error = f"Fehler bei all_stocks_by_customer:\nsql: {sql}\n" \
                f"customer_id: {customer_id}\nisin: {isin}\nError: {e}\n"
        print(error)
        result = f"Kein Eintrag gefunden, Error: {e}"

    finally:
        db_op.close()
        return result


def update_single_stock_datas(isin):

    stock_info = simple_search("stocks", "isin", isin)

    ticker_symbol = f"{stock_info["row_result0"]["ticker_symbol"]}.DE"
    ticker_data = yf.Ticker(ticker_symbol)
    historical_data = ticker_data.history(period='1d')

    row = historical_data.iloc[0]

    # date = str(row.name.strftime('%Y-%m-%d'))

    values = (row['Open'],
              row['High'],
              row['Low'],
              row['Close'],
              row['Volume'],
              row['Dividends'],
              row['Stock Splits'],
              isin,
              row.name.strftime('%Y-%m-%d')
              )

    sql = """UPDATE stock_data
                SET open = ?,
                    high = ?,
                    low = ?,
                    close = ?,
                    volume = ?,
                    dividends = ?,
                    stock_splits = ?
                WHERE isin = ? and date = ?"""

    db_op.open_connection_db()
    db_op.execute_and_commit(sql, values)
    db_op.close()
