from .db_executor import DBExecutor

from .repo_utilitys import make_dictionary

db_ex = DBExecutor()


def insert_stock_transaction(transaction: dict, balance: dict):
    print("start insert stock transaction")
    try:
        db_ex.open_connection_db()
        db_ex.start_transaction()

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
        transaction_id = db_ex.execute(sql, transaction).lastrowid

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

        balance_id = db_ex.execute(sql, balance).lastrowid

        db_ex.connection_commit()
        print("ende try stock transaction")

    except Exception as e:
        error = f"Fehler bei insert_stock_transaction(" \
                f"transaction:dict: {transaction},"\
                f"balance:dict: {balance}).\nError: {e}"
        print(error)
        db_ex.rollback()
        raise ValueError(error)

    finally:
        db_ex.close()
        return transaction_id, balance_id


def stock_transactions_overview(customer_id):

    db_ex.open_connection_db()
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
                                    WHERE isin=t.isin
                                        AND transaction_type = 'buy')
                                        AS amount,
                            SUM (t.amount * t.price_per_stock) / SUM(t.amount)
                                AS price_per_stock_all,
                            (SELECT sd.close
                                FROM stock_data sd
                                WHERE isin = t.isin
                                ORDER BY date DESC
                                LIMIT 1) AS actual_price
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
                                    WHERE isin=t.isin
                                        AND transaction_type = 'sell')
                                        AS amount
                        FROM transactions t
                        WHERE t.customer_id = ? and transaction_type = 'sell'
                        GROUP BY t.isin
                    ) AS sell ON buy.isin = sell.isin"""

        value = (customer_id, customer_id,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result = make_dictionary(datas, names)

        print(f"result ist : {result}")

        return result

    except Exception as e:
        error = f"Fehler bei stock_transactions_overview:\nsql: {sql}\n" \
                f"customer_id: {customer_id}\nError: {e}\n"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()


def search_past_transactions(customer_id, search_start, search_end):

    db_ex.open_connection_db()

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
                        WHERE t.customer_id = ?
                            AND DATE(t.transaction_date) >= ?
                            AND DATE(t.transaction_date) <= ?
                        GROUP by t.transaction_date
                        ORDER BY t.transaction_date ASC
                    ) AS t
                    LEFT JOIN (
                        SELECT s.isin, s.company_name as company_name
                        FROM stocks AS s
                        ) AS s
                        ON t.isin = s.isin"""

        value = (customer_id, search_start, search_end,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result = make_dictionary(datas, names)

        print(f"result ist : {result}")

        return result

    except Exception as e:
        error = f"Fehler bei search_past_transactions:\nsql: {sql}\n" \
                f"customer_id: {customer_id}\nsearch_start: {search_start}\n" \
                f"search_end: {search_end}\nError: {e}\n"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()


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
