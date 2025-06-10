from utilities import DBOperationError, SQLExecutionError, make_dictionary

# db_op - Instanz von DBOperator
from .db_operator import db_op


def watchlist_overview(customer_id):

    try:
        db_op.open_connection_db()

        sql = """SELECT
                    w.isin AS isin,
                    w.price AS price ,
                    (SELECT stocks.company_name
                        FROM stocks
                        WHERE isin = w.isin
                        ) AS company_name,
                    (SELECT close
                        FROM stock_data
                        WHERE isin = w.isin
                        ORDER BY date DESC LIMIT 1
                        ) AS current_price,
                    ((SELECT close
                        FROM stock_data
                        WHERE isin = w.isin
                        ORDER BY date DESC LIMIT 1) / w.price) AS performance,
                    w.date
                    FROM watchlist AS w
                    WHERE w.customer_id = ?"""
        value = (customer_id,)
        datas = db_op.execute(sql, value).fetchall()

        names = db_op.col_names()

        result = make_dictionary(datas, names)

        return result

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            f"Fehler bei Datenbankabfrage:\n"
            f"customer_id: {customer_id}\n"
            f"SQL: {sql}"
            f"Ort: watchlist_overview (watchlist_repo.py)"
            f"Error: {str(e)}\n")
        raise SQLExecutionError(error_msg) from e

    finally:
        db_op.close()


if __name__ == "__main__":

    answer = watchlist_overview(1)

    print(" ")
    print(answer)
