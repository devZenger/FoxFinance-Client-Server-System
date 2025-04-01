from .db_executor import DBExecutor

db_ex = DBExecutor()


def make_dictionary(datas, names):

    search_result = {}
    i = 0
    for data in datas:
        row_data = {}
        for j in range(len(data)):
            row_data[names[j]] = data[j]

        search_result[f"row_result{i}"]= row_data
        i += 1

    return search_result


def make_dictionary_one_result(datas, names):
    row_data = {}
    for j in range(len(datas)):
        row_data[names[j]] = datas[j]

    return row_data


def simple_search(table, column, search_term):

    try:
        db_ex.open_connection_db()

        sql = f"""SELECT * FROM {table} WHERE {column} LIKE ?"""
        value = (search_term,)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result = make_dictionary(datas, names)

        return result

    except Exception as e:
        error = f"Fehler bei simple_search, table:{table},"\
                f"column:{column}, search_term:{search_term}.\nError:{e}"
        print(error)
        raise Exception(error)

    finally:
        db_ex.close()



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
