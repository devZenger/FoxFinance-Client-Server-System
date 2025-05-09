from .db_executor import DBExecutor
from .repo_utilitys import make_dictionary

db_ex = DBExecutor()


def customer_balance(customer_id):

    try:
        db_ex.open_connection_db()

        sql = """SELECT
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id
                        = 1), 0) +
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id
                        = 4), 0) -
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id
                        = 2), 0) -
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id
                        = 3), 0)
                AS actual_balance"""

        value = (customer_id, customer_id, customer_id, customer_id,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        dic = {}
        dic[names[0]] = datas[0][0]

        return dic

    except Exception as e:
        error = f"Fehler bei customer_balance:\nsql: {sql}" \
                f"customer_id: {customer_id}.\nError: {e}\n"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()


def search_past_financial_transactions(customer_id, search_start, search_end):

    db_ex.open_connection_db()

    try:
        sql = """SELECT
                    ft.fin_transaction_date,
                    ftt.fin_transaction_type,
                    ft.fin_amount,
                    ft.bank_account
                    FROM (
                        SELECT *
                        FROM financial_transactions AS ft
                        WHERE ft.customer_id = ?
                            AND DATE(ft.fin_transaction_date) >= ?
                            AND DATE(ft.fin_transaction_date) <= ?
                        ORDER BY ft.fin_transaction_date ASC
                    ) AS ft
                    LEFT JOIN (
                        SELECT ftt.fin_transaction_type_id
                        , ftt.fin_transaction_type
                        FROM fin_transaction_types AS ftt
                        )AS ftt
                        ON ft.fin_transaction_type_id
                         = ftt.fin_transaction_type_id
                        """

        value = (customer_id, search_start, search_end,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result = make_dictionary(datas, names)

        print(f"result ist : {result}")

        return result

    except Exception as e:
        error = f"Fehler bei search_past_financial_transactions:\nsql: " \
                f"{sql}\ncustomer_id: {customer_id}, search_start: " \
                f"{search_start}\nsearch_end: {search_end}\nError: {e}"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()


def insert_bank_transfer(b_transfer: dict):

    db_ex.open_connection_db()
    db_ex.start_transaction()

    try:
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

        balance_id = db_ex.execute(sql, b_transfer).lastrowid

        db_ex.connection_commit()

        return balance_id
    except Exception as e:
        db_ex.rollback()
        error = f"Fehler bei insert_bank_transfer:\n" \
                f"b_transfer:dict:{b_transfer})\nError: {e}"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()


if __name__ == "__main__":

    print("start")
    table = "stocks"

    isin = "DE0005190003"
    customer_id = 1

    transfer = {"customer_id": 1,
                "bank_account": "zoe",
                "fin_amount": 500.0,
                "fin_transaction_type_id": 1,
                "usage": "test"}

    answer = insert_bank_transfer(transfer)

    print(answer)
