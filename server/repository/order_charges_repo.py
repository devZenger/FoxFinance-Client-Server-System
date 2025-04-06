from .db_executor import DBExecutor

from .search_repo import make_dictionary_one_result, make_dictionary

db_ex = DBExecutor()


def search_order_charges(volumn, date):

    try:
        db_ex.open_connection_db()

        sql = """SELECT *
                FROM order_charges
                WHERE start_validation <= ?
                    AND ? <= end_validation
                    AND ? >= min_volumn
                ORDER BY min_volumn DESC
                LIMIT 1"""
        value = (date, date, volumn)
        datas = db_ex.execute(sql, value).fetchall()

        names = db_ex.col_names()

        result = make_dictionary_one_result(datas[0], names)

    except Exception as e:
        error = f"Fehler bei search_order_charges(volumn: {volumn}," \
                f"date: {date})\n.Error: {e}"
        print(error)
        result = "Kein Eintrag gefunden, Error: {e}"

    finally:
        db_ex.close()
        return result


def search_all_order_charges(date):
    
    try:
        db_ex.open_connection_db()
        
        sql = """SELECT *
                 FROM order_charges
                 WHERE start_validation <= ?
                    AND end_validation >= ?
                 ORDER BY min_volumn"""
        
        value = (date, date)
        
        datas = db_ex.execute(sql, value).fetchall()
        
        names = db_ex.col_names()
        
        print("datas", datas)
        
        result = make_dictionary(datas, names)
        
        return result
        
    except Exception as e:
        error = f"Fehler bei search_all_order_charges, sql: {sql}," \
                f"date: {date})\n.Error: {e}\n"
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

    date = "2021-5-21"
    volumn = 324

    answer = search_all_order_charges(date)

    print(answer)
