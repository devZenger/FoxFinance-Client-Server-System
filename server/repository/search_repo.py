from utilities import DBOperationError, SQlExecutionError, make_dictionary

# db_op - Instanz von DBOperator
from .db_operator import db_op


def simple_search(table, column, search_term):

    try:
        db_op.open_connection_db()

        sql = f"""SELECT * FROM {table} WHERE {column} LIKE ?"""
        value = (search_term,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        result = make_dictionary(datas, names)

        return result

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            f"Fehler bei simple_search:\n"
            f"Tabelle: {table}\n"
            f"Spalte:{column}\n"
            f"Suchbegriff:{search_term}\n"
            f"SQL: {sql}"
            "Ort: simple_search (search_repo)"
            f"Error: {e}")
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "isin"
    search_term = "DE0005190003"
    time = "6 months"

    answer = simple_search(table, column, search_term)

    print(" ")
    print(answer)

    print(" ")
    stocks_row = answer["row_result0"]
    print(stocks_row)
