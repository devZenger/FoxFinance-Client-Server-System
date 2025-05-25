from utilities import DBOperationError, SQlExecutionError

# db_op - Instanz von DBOperator
from .db_operator import db_op


def update_one_table(table, update: dict, condition_dic: dict):

    db_op.open_connection_db()

    columns = ""
    for k in update.keys():
        columns = f"{columns}{k}= :{k}, "
    columns = columns[:-2]

    condition = ""
    for k in condition_dic.keys():
        condition = f"{condition}{k}=:{k} and "
    condition = condition[:-5]

    try:
        sql = f"""UPDATE {table}
                    SET {columns}
                    WHERE {condition}"""

        values = update
        values.update(condition_dic)

        db_op.execute_and_commit(sql, values)

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler beim Update der Datenbanktabelle:\n"
            f"Tabelle: {table}\n"
            f"Bedingung (dict): {condition_dic}\n"
            f"SQL: {sql}\n"
            "Ort: update_one_table (update_repo)\n" \
            f"update:{update}\ncondition_dic:{condition_dic}\n"
            f"Error:{str(e)}\n"
            )
        raise SQlExecutionError(error_msg) from e
