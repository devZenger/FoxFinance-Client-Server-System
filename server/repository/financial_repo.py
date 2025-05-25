from utilities import DBOperationError, SQlExecutionError, make_dictionary

# db_op - Instanz von DBOperator
from .db_operator import db_op


def customer_balance(customer_id):

    try:
        db_op.open_connection_db()

        sql = """SELECT
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id = 1), 0) +
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id = 4), 0) -
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id = 2), 0) -
                    COALESCE((SELECT SUM(fin_amount)
                        FROM financial_transactions
                        WHERE customer_id = ? AND fin_transaction_type_id = 3), 0)
                AS actual_balance"""

        value = (customer_id, customer_id, customer_id, customer_id,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        dic = {}
        dic[names[0]] = datas[0][0]

        return dic

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler bei Datenbankabfrage:\n"
            f"customer_id: {customer_id}\n"
            f"SQL: {sql}"
            f"Ort: customer_balance (financial_repo.py)"
            f"Error: {e}\n")
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


def search_past_financial_transactions(customer_id, search_start, search_end):

    db_op.open_connection_db()

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
                        SELECT ftt.fin_transaction_type_id, ftt.fin_transaction_type
                        FROM fin_transaction_types AS ftt
                        )AS ftt
                        ON ft.fin_transaction_type_id = ftt.fin_transaction_type_id"""

        value = (customer_id, search_start, search_end,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        result = make_dictionary(datas, names)

        return result

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler bei der Datenabfrage:\n"
            f"customer_id: {customer_id}\n"
            f"Suchstart: {search_start}\n"
            f"Suchende: {search_end}\n"
            f"SQL: {sql}\n"
            f"Ort: search_past_financial_transactions (financial_repo.py)\n"
            f"Error: {e}\n")
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


def insert_bank_transfer(b_transfer: dict):

    db_op.open_connection_db()
    db_op.start_transaction()

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

        balance_id = db_op.execute(sql, b_transfer).lastrowid

        db_op.connection_commit()

        return balance_id

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        db_op.rollback()
        error_msg = (
            f"Fehler bei einfügen eines Banktransfers:\n"
            f"Transfer (dict): {b_transfer})\n"
            f"SQL: {sql}\n"
            f"Ort: insert_bank_transfer (financial_repo.py)\n"
            f"Error: {e}\n"
            )
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


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
