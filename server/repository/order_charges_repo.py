from utilities import (DBOperationError,
                       SQLExecutionError,
                       make_dictionary,
                       make_dictionary_one_result,
                       error_forwarding_msg)

# db_op - Instanz von DBOperator
from .db_operator import db_op


def search_order_charges(volume, date):

    try:
        db_op.open_connection_db()

        sql = """SELECT *
                FROM order_charges
                WHERE start_validation <= ? AND ? <= end_validation AND ? >= min_volumn
                ORDER BY min_volumn DESC
                LIMIT 1"""
        value = (date, date, volume)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()
        result = make_dictionary_one_result(datas[0], names)

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except Exception as e:
        error_msg = (
            f"Fehler bei Abfrage nach Ordergebühren:\n"
            f"Volumen: {volume}\n"
            f"date: {date})\n."
            f"SQL: {sql}\n"
            "Ort: search_order_charges (order_charges_repo.py)"
            f"Error: {str(e)}\n")
        raise SQLExecutionError(error_msg) from e

    finally:
        db_op.close()
        return result


def search_all_order_charges(date):

    try:
        db_op.open_connection_db()

        sql = """SELECT *
                 FROM order_charges
                 WHERE start_validation <= ? AND end_validation >= ?
                 ORDER BY min_volumn"""
        value = (date, date)

        datas = db_op.execute(sql, value).fetchall()
        names = db_op.col_names()

        result = make_dictionary(datas, names)

        return result

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except Exception as e:
        error_msg = (
            f"Fehler bei der Abfrage nach allen Ordergebühren:\n"
            f"date: {date})\n"
            f"SQL: {sql}\n"
            "Ort: search_all_order_charges (order_charges_repo.py)\n"
            f"Error: {e}\n")
        raise SQLExecutionError(error_msg)

    finally:
        db_op.close()


if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "isin"

    search_term = "DE0005190003"
    time = "6 months"

    date = "2021-5-21"
    volume = 324

    answer = search_order_charges(volume, date)

    print(answer)
