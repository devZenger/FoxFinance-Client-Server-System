from .db_executor import DBExecutor


def simple_search(table, column, search_term):

    db_ex = DBExecutor()

    db_ex.open_connection_db()

    try:
        sql = f"""SELECT * FROM {table} WHERE {column} LIKE ?"""
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        search_result = {}
        row_data = {}
        i = 0
        for data in datas:
            print(f"data: {data}")
            row_data = {}
            for j in range(len(data)):
                row_data[names[j]] = data[j]
                print(f"{j} {data[j]}")
                print("-------")

            search_result[f"row_result{i}"] = row_data
            print(f"search {search_result} i = {i}")
            i += 1

        return search_result

    except Exception as e:
        error = f"Fehler bei simple_search:\nsql: {sql}\ntable: {table}\n" \
                f"column: {column}\nsearch_term: {search_term}\n" \
                f"\nError: {e}\n"
        print(error)
        return None

    finally:
        db_ex.close()


if __name__ == "__main__":

    print("start")
    table = "stocks"
    column = "company_name"
    search_term = "%%deutsche%%"

    answer = simple_search(table, column, search_term)

    print(" ")

    print(len(answer))
    print(answer)
