from utilitys import DBOperationError, SQlExecutionError

# db_op - Instanz von DBOperator
from .db_operator import db_op


def get_auth_datas(email):

    try:
        db_op.open_connection_db()

        sql = """SELECT * FROM customers WHERE email= ?"""
        value = (email,)
        data = db_op.execute(sql, value).fetchall()

        if not data:
            return None

        data = data[0]
        names = db_op.col_names()

        auth_dic = {}
        for i in range(len(data)):
            auth_dic[names[i]] = data[i]

        sql = """SELECT password
                 FROM authentication
                 WHERE customer_id = ?"""

        value = (auth_dic["customer_id"],)

        data = db_op.execute(sql, value).fetchall()
        data = data[0]
        names = db_op.col_names()
        for i in range(len(data)):
            auth_dic[names[i]] = data[i]

        return auth_dic

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler bei Datenbankabfrage:\n"
            f"Suchbegriff: {email}\n"
            f"SQL: {sql}\n"
            f"Position: get_auth_datas:\n"
            f"Error: {e}\n"
            )
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


def insert_login_time(customer_id):
    try:
        value = (customer_id,)
        db_op.open_connection_db()
        sql = """UPDATE customers SET last_login = CURRENT_TIMESTAMP
                    WHERE customer_id = ?"""

        db_op.execute_and_commit(sql, value)

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler beim Update der Spalte login_time:\n"
            f"customer_id: {customer_id}\n"
            f"SQL: {sql}\n"
            f"Ort: insert_login_time (authentication_repo.py)\n"
            f"Error: {e}\n"
            )
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


if __name__ == "__main__":

    print("start")
    email = "zoe"

    customer_id = 1

    answer = get_auth_datas(email)

    print(" ")
    print(answer)
    print(" ")
