from .db_executor import DBExecutor

db_ex = DBExecutor()


def get_auth_datas(email):

    try:
        db_ex.open_connection_db()

        sql = """SELECT * FROM customers WHERE email= ?"""
        value = (email,)
        data = db_ex.execute(sql, value).fetchall()

        if not data:
            return None
        
        data = data[0]
        names = db_ex.col_names()

        auth_dic = {}
        for i in range(len(data)):
            auth_dic[names[i]] = data[i]

        sql = """SELECT password
                 FROM authentication
                 WHERE customer_id = ?"""

        value = (auth_dic["customer_id"],)

        data = db_ex.execute(sql, value).fetchall()
        data = data[0]
        names = db_ex.col_names()
        for i in range(len(data)):
            auth_dic[names[i]] = data[i]

        return auth_dic

    except Exception as e:
        error = f"Position: get_auth_datas:\nsql: {sql}" \
                f"\nemail: {email}.\nError: {e}\n"
        print(error)
        raise Exception(error)

    finally:
        db_ex.close()


def insert_login_time(customer_id):
    try:
        db_ex.open_connection_db()
        sql = f"""UPDATE customers SET last_login = CURRENT_TIMESTAMP
                    WHERE customer_id = '{customer_id}'"""

        db_ex.execute_and_commit_just_sql(sql)

    except Exception as e:
        error = f"Fehler bei insert_login_time:\nsql:{sql}\n" \
                f"customer_id: {customer_id}\nError: {e}\n"
        print(error)
        raise Exception(error)

    finally:
        db_ex.close()


if __name__ == "__main__":

    print("start")
    email = "zoe"

    customer_id = 1

    answer = get_auth_datas(email)

    print(" ")
    print(answer)
    print(" ")
