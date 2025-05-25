import sqlite3
import os
from logger import status_message
from utilitys import DBOperationError
import utilitys.config_loader

# DBOperator Instanz unten


class DBOperator:
    def __init__(self):
        self.path = utilitys.config_loader.path_db
        self.cursor = None
        self.connection = None

    def open_connection_db(self):
        try:
            if not os.path.exists(self.path):
                utilitys.config_loader.load_config()
                self.path = utilitys.config_loader.path_db

            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            status_message("Mit Datenbank verbunden")
        except sqlite3.Error as e:
            error_msg = (
                "Verbindungsprobleme mit der Datenbank:\n"
                "Ort: open_connection_db (db_operator.py)"
                f"Error: {str(e)}\n")
            raise DBOperationError(error_msg) from e

    def start_transaction(self):
        try:
            self.connection.execute("BEGIN TRANSACTION")
        except sqlite3.Error as e:
            error_msg = (
                "Fehler beim Ausführen des Transaction-Kommandos.\n"
                "Ort: rollback (db_executor.py)\n"
                f"Error: {str(e)}\n")
            raise DBOperationError(error_msg) from e

    def connection_commit(self):
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            error_msg = (
                "Fehler beim Ausführen eines Commit-Kommandos"
                "Ort: connection_commit (db_executor.py)"
                f"Error: {str(e)}\n"
                )
            raise DBOperationError(error_msg) from e

    def rollback(self):
        try:
            self.connection.rollback()
        except sqlite3.Error as e:
            error_msg = (
                "Fehler beim Ausführen des Rollback-Kommandos.\n"
                "Ort: rollback (db_executor.py)"
                f"Error: {str(e)}\n"
                )
            raise DBOperationError(error_msg) from e

    def execute(self, sql, value=None):
        try:
            if value is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, value)
        except sqlite3.Error as e:
            if value is None:
                error_msg = (
                    f"Fehler beim Ausführen eines SQL-Kommandos:\n"
                    f"SQL: {sql}.\n"
                    f"Ort: execute (db_executor.py)\n"
                    f"Error: {str(e)}\n"
                    )
            else:
                error_msg = (
                    f"Fehler beim Ausführen eines SQL-Kommandos:\n"
                    f"SQL: {sql}\n"
                    f"Werte: {value}\n"
                    f"Ort: execute (db_executor.py)\n"
                    f"Error: {str(e)}\n"
                    )
            raise DBOperationError(error_msg) from e
        return self.cursor

    def execute_and_commit(self, sql, value=None):
        try:
            if value is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, value)
            self.connection.commit()
        except sqlite3.Error as e:
            if value is None:
                error_msg = (
                    f"Fehler beim Ausführen bzw. Commit eines SQL-Kommandos:\n"
                    f"SQL: {sql}.\n"
                    f"Ort: execute_and_commit (db_executor.py)\n"
                    f"Error: {str(e)}"
                    )
            else:
                error_msg = (
                    f"Fehler beim Ausführen bzw. Commit eines SQL-Kommandos:\n"
                    f"SQL: {sql}\n"
                    f"Werte: {value}\n"
                    f"Ort: execute_and_commit (db_executor.py)\n"
                    f"Error: {str(e)}\n"
                    )
            raise DBOperationError(error_msg) from e
        return self.cursor

    def execute_return_bool(self, sql, values):
        success = False
        try:
            self.cursor.execute(sql, values)
            success = True

        except Exception:
            success = False

        finally:
            if success:
                self.connection.commit()

        return success

    def col_names(self):
        col_name = []
        names = self.cursor.description
        for name in names:
            col_name.append(name[0])

        return col_name

    def close(self):
        self.connection.close()


# Globale Instanz
db_op = DBOperator()
