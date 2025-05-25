from utilitys import DBOperationError, SQlExecutionError

# db_op - Instanz von DBOperator
from .db_operator import db_op


def insert_customer(input):

    db_op.open_connection_db()

    try:
        db_op.start_transaction()

        input["disabled"] = False
        input["bank_account"] = input["reference_account"]
        input["fin_transaction_type_id"] = 1
        input["usage"] = "Depoteröffnung"

        sql = """INSERT INTO customers(
                    first_name,
                    last_name,
                    email,
                    phone_number,
                    birthday)
                    VALUES(
                    :first_name,
                    :last_name,
                    :email,
                    :phone_number,
                    :birthday
            )"""
        customer_id = db_op.execute(sql, input).lastrowid
        input["customer_id"] = customer_id

        sql = """INSERT INTO customer_adresses VALUES(
                    :customer_id,
                    :street,
                    :house_number,
                    :zip_code,
                    :city)"""
        db_op.execute(sql, input)

        sql = """INSERT INTO authentication VALUES(
                    :customer_id,
                    :password)"""
        db_op.execute(sql, input)

        sql = """INSERT INTO financials VALUES(
                    :customer_id,
                    :reference_account)"""
        db_op.execute(sql, input)

        sql = """INSERT INTO financial_transactions
                    (customer_id,
                    bank_account,
                    fin_amount,
                    fin_transaction_type_id,
                    usage)
                    VALUES(
                    :customer_id,
                    :bank_account,
                    :fin_amount,
                    :fin_transaction_type_id,
                    :usage)"""
        db_op.execute(sql, input)

        db_op.connection_commit()

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        db_op.rollback()
        error_msg = (
                "Fehler beim Einfügen von Kundendaten\n"
                f"Eingabe: {input}\n"
                f"SQL: {sql}\n"
                f"Ort: update_customer_settings (customer_repo.py)"
                f"Error: {e}\n")
        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


def update_customer_settings(table, customer_id, insert: dict):

    db_op.open_connection_db()

    try:

        columns = ""
        for k in insert.keys():
            columns = f"{columns}{k}=:{k}, "

        columns = columns[:-2]

        values = insert.copy()
        values["customer_id"] = customer_id

        sql = f"""UPDATE {table}
                    SET {columns}
                    WHERE customer_id=:customer_id"""

        db_op.execute_and_commit(sql, values)

    except DBOperationError as e:
        raise DBOperationError("Fehler während der Datenbankoperation") from e
    except Exception as e:
        error_msg = (
            "Fehler beim Update der Kundendaten update_customer_settings.\n"
            f"customer_id{customer_id}\n"
            f"table: {table}\n"
            f"Update-Daten: {insert}\n"
            f"SQL: {sql}\n"
            f"Ort: update_customer_settings (customer_repo.py)"
            f"Error: {e}\n")

        raise SQlExecutionError(error_msg) from e

    finally:
        db_op.close()


if __name__ == "__main__":

    dic = {'reference_account': 'z-bank'}
    table = "financials"
    test = update_customer_settings(table, 1, dic)
