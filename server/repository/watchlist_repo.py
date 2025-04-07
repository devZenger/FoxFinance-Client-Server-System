from .db_executor import DBExecutor

from .search_repo import make_dictionary

db_ex = DBExecutor()


def watchlist_overview(customer_id):

    try:
        db_ex.open_connection_db()

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
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result = make_dictionary(datas, names)

        return result

    except Exception as e:
        error = f"Fehler bei watchlist_overview:\nsql: {sql}\n" \
                f"customer_id: {customer_id}\nError: {e}\n"
        print(error)
        raise ValueError(error)

    finally:
        db_ex.close()


if __name__ == "__main__":

    answer = watchlist_overview(1)

    print(" ")
    print(answer)
