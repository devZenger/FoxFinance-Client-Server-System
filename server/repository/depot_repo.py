from .db_executor import DBExecutor

db_ex = DBExecutor()


def customer_balance(customer_id):

    try:
        db_ex.open_connection_db()

        sql = """SELECT
                 COALESCE((SELECT SUM(isin, amount)
                    FROM balance_transactions
                    WHERE customer_id = ?
                        AND balance_transaction_type_id = 1), 0) -
                 COALESCE((SELECT SUM(isin, amount)
                    FROM balance_transactions
                    WHERE customer_id = ?
                        AND balance_transaction_type_id = 2), 0)
                 AS actual_depot"""

        value = (customer_id, customer_id, customer_id, customer_id,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        dic = {}
        dic[names[0]] = datas[0][0]

        return dic

    except Exception as e:
        error = f"Fehler bei customer_balance, customer_id:\nsql: {sql}\n" \
                f"customer_id: {customer_id}\nError: {e}\n"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()
