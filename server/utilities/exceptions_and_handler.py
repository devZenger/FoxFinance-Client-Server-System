from fastapi import HTTPException

from logger import error_message, http442_message
from .check_and_error_msg import error_msg_db_sql, error_msg_no_service


class DBOperationError(Exception):
    # Fehler bei der Nutzung von DBExecutor.
    pass


class SQLExecutionError(Exception):
    # Fehler beim Ausführen von SQL.
    pass


class StockDataFetchError(Exception):
    # Fehler bei Abruf von 'yfinance'
    pass


class NoneOrEmptyError(ValueError):
    # Fehler bei leeren oder None Variblen
    pass


def excptions_handler(e: Exception, msg: str):

    if isinstance(e, ValueError):
        message_msg = (f"Oberstes Modul: {msg}.\n"
                       f"Error: {str(e)}")
        detail_msg = "Ungültige Eingaben. Es tut und leid, Ihre Anfrage konnte nicht verarbeitet werden."
        http442_message(e, message_msg)
        raise HTTPException(status_code=422, detail=detail_msg)
    elif isinstance(e, (DBOperationError, SQLExecutionError)):
        error_message(e)
        raise HTTPException(status_code=500, detail=error_msg_db_sql)
    else:
        error_message(e, msg)
        raise HTTPException(status_code=500, detail=error_msg_no_service)
