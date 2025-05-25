from utilities import DBOperationError, SQlExecutionError, make_dictionary

# db_op - Instanz von DBOperator
from .db_operator import db_op


def insert_stock_transaction(transaction: dict, balance: dict):
    print("start insert stock transaction")
    try:
        db_op.open_connection_db()
        db_op.start_transaction()

        sql = """INSERT INTO transactions(
                 customer_id,
                 isin,
                 transaction_type,
                 amount,
                 price_per_stock,
                 order_charge_id) VALUES(
                 :customer_id,
                 :isin,
                 :transaction_type,
                 :amount,
                 :price_per_stock,
                 :order_charge_id
                 )"""
        transaction_id = db_op.execute(sql, transaction).lastrowid

        balance["usage"] = f"Aktientransaktions Nr.: {transaction_id}"

        sql = """INSERT INTO financial_transactions(
                 customer_id,
                 bank_account,
                 fin_amount,
                 fin_transaction_type_id,
                 usage) VALUES (
                 :customer_id,
                 :bank_account,
                 :fin_amount,
                 :fin_transaction_type_id,
                 :usage)"""

        balance_id = db_op.execute(sql, balance).lastrowid

        db_op.connection_commit()
        print("ende try stock transaction")

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = f"Fehler bei insert_stock_transaction(" \
                f"transaction:dict: {transaction},"\
                f"balance:dict: {balance}).\nError: {e}"

        db_op.rollback()
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()
        return transaction_id, balance_id


def stock_transactions_overview(customer_id):

    db_op.open_connection_db()
    try:
        sql = """SELECT
                    buy.isin AS isin,
                    buy.company_name AS company_name,
                    buy.amount - coalesce(sell.amount, 0) AS amount,
                    buy.price_per_stock_all AS price_per_stock,
                    buy.actual_price As actual_price,
                    (buy.actual_price / buy.price_per_stock_all) AS performance
                    FROM(
                        SELECT
                            t.isin AS isin,
                            s.company_name AS company_name,
                            (SELECT SUM(t.amount)
                                    FROM transactions
                                    WHERE isin=t.isin AND transaction_type = 'buy')
                                    AS amount,
                            SUM (t.amount * t.price_per_stock) / SUM(t.amount)
                                AS price_per_stock_all,
                            (SELECT sd.close
                                FROM stock_data sd
                                WHERE isin = t.isin
                                ORDER BY date DESC
                                LIMIT 1)
                                AS actual_price
                        FROM transactions t
                        JOIN stocks s ON t.isin = s.isin
                        WHERE t.customer_id = ? and transaction_type = 'buy'
                        GROUP BY t.isin, s.company_name
                    ) AS buy
                    LEFT JOIN (
                        SELECT
                            t.isin AS isin,
                            (SELECT SUM(t.amount)
                                    FROM transactions
                                    WHERE isin=t.isin AND transaction_type = 'sell')
                                    AS amount
                        FROM transactions t
                        WHERE t.customer_id = ? and transaction_type = 'sell'
                        GROUP BY t.isin
                    ) AS sell ON buy.isin = sell.isin
                    WHERE (buy.amount - coalesce(sell.amount, 0)) > 0"""

        value = (customer_id, customer_id,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        result = make_dictionary(datas, names)

        return result

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler bei Datenbankabfrage:\n"
            f"customer_id: {customer_id}\n"
            f"SQL: {sql}\n"
            "Ort: stock_transactions_overview (transaction_repo.py)"
            f"Error: {e}\n")
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


def search_past_transactions(customer_id, search_start, search_end):

    db_op.open_connection_db()

    try:
        sql = """SELECT
                    t.transaction_id,
                    t.transaction_date,
                    t.transaction_type,
                    t.isin,
                    s.company_name,
                    t.amount,
                    t.price_per_stock
                    FROM (
                        SELECT *
                        FROM transactions AS t
                        WHERE t.customer_id = ? AND DATE(t.transaction_date) >= ? AND DATE(t.transaction_date) <= ?
                        GROUP by t.transaction_date
                        ORDER BY t.transaction_date ASC
                    ) AS t
                    LEFT JOIN (
                        SELECT s.isin, s.company_name as company_name
                        FROM stocks AS s
                        ) AS s
                        ON t.isin = s.isin"""

        value = (customer_id, search_start, search_end,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        result = make_dictionary(datas, names)

        return result

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            f"Fehler bei search_past_transactions:\n"
            f"customer_id: {customer_id}\n"
            f"search_start: {search_start}\n"
            f"search_end: {search_end}\n"
            f"SQL: {sql}\n"
            "Ort: search_past_transaction (transaction_repo.py)"
            f"Error: {e}\n")
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


if __name__ == "__main__":

    print("start")
    start = "2025-01-12"
    end = "2025-05-13"
    table = "stocks"
    column = "company_name"
    search_term = "%%deutsche%%"

    answer = search_past_transactions(101, start, end)

    print(" ")

    print(len(answer))
    print(answer)
