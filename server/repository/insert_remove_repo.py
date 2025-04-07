from .db_executor import DBExecutor

db_ex = DBExecutor()


def key_to_column(to_form: dict):

    key_str = ""
    for k in to_form.keys():
        key_str = f"{key_str}{k},"

    return key_str[:-1]


def key_to_value(to_form: dict):

    key_str = ""
    for k in to_form.keys():
        key_str = f"{key_str} :{k},"

    return key_str[:-1]


def key_to_where(to_form: dict):
    key_str = ""
    for k in to_form.keys():
        key_str = f"{key_str} {k}=:{k} and"

    return key_str[:-3]


def insert_one_table(table, insert: dict):

    try:
        db_ex.open_connection_db()

        key_column = key_to_column(insert)
        key_value = key_to_value(insert)

        sql = f"""INSERT INTO {table} ({key_column}) VALUES({key_value})"""
        execute_id = db_ex.execute_and_commit(sql, insert).lastrowid

        return execute_id

    except Exception as e:
        error = f"Fehler bei insert_one_table:\nsql:{sql}\ntable:" \
                f"{table}\ninsert: {insert}.\nError: {e}\n"
        print(error)
        raise Exception(error)

    finally:
        db_ex.close


def remove_from_one_table(table, condition: dict):

    try:
        key_condition = key_to_where(condition)
        db_ex.open_connection_db()

        sql = f"""DELETE FROM {table} WHERE {key_condition}"""

        db_ex.execute_and_commit(sql, condition)

    except Exception as e:
        error = f"Fehler bei delete_from_one_table\nsql: {sql}\n" \
                f"table: {table}\ncondition: {condition}.\nError: {e}\n"
        print(error)
        raise Exception(error)


if __name__ == "__main__":

    print("start")
    input = {"customer_id": 3}
    update = {"validation_number": 343434}

    input.update(update)

    answer = insert_one_table("validation", input)

    print(answer)
