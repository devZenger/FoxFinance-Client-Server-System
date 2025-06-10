from utilities import DBOperationError, SQLExecutionError, error_forwarding_msg

# db_op - Instanz von DBOperator
from .db_operator import db_op


def insert_one_table(table, insert: dict):

    try:
        db_op.open_connection_db()

        key_list_c = []
        key_list_v = []
        for k in insert.keys():
            key_list_c.append(f"{k}")
            key_list_v.append(f":{k}")
        key_column = ",".join(key_list_c)
        key_value = ",".join(key_list_v)

        sql = f"""INSERT INTO {table} ({key_column}) VALUES({key_value})"""
        execute_id = db_op.execute_and_commit(sql, insert).lastrowid

        return execute_id

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except Exception as e:
        error_msg = (
            "Fehler beim Einfügen in einer Datenbanktabelle:"
            f"Tabelle: {table}\n"
            f"Eingabedaten: {insert}\n"
            f"SQL: {sql}\n"
            "Ort: insert_one_table (insert_remove_repo.py)\n"
            f"Error: {e}\n")
        raise SQLExecutionError(error_msg) from e

    finally:
        db_op.close


def remove_from_one_table(table, condition: dict):

    try:
        key_list = []
        for k in condition.keys():
            key_list.append(f"{k}=:{k}")

        key_condition = " and ".join(key_list)

        db_op.open_connection_db()

        sql = f"""DELETE FROM {table} WHERE {key_condition}"""

        db_op.execute_and_commit(sql, condition)

    except DBOperationError as e:
        raise DBOperationError(error_forwarding_msg) from e
    except Exception as e:
        error_msg = (
            "Fehler bim Entfernen eines Datensatzes:"
            f"Tabelle: {table}\n"
            f"Bedingung: {condition}\n"
            f"SQL: {sql}\n"
            "Ort: delete_from_one_table (insert_remove_repo.py)\n"
            f"Error: {e}\n")
        raise SQLExecutionError(error_msg) from e

    finally:
        db_op.close()


if __name__ == "__main__":

    print("start")
    input = {"customer_id": 3}
    update = {"validation_number": 343434}

    input.update(update)

    answer = insert_one_table("validation", input)

    print(answer)
