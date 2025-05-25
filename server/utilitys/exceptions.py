error_msg_no_service = (
    "Es tut uns leid, ein unerwarteter Fehler ist aufgetreten\n"
    "\tDer Service steht derzeit nicht zur Verfügung\n"
    "\tWir bitten um Ihr Verständnis\n"
    "\tViele Grüsse, das FoxFinance Team")


class DBOperationError(Exception):
    # Fehler bei der Nutzung von DBExecutor.
    pass


class SQlExecutionError(Exception):
    # Fehler beim Ausführen von SQL.
    pass


class ValidationError(Exception):
    # Fehler bei Prüfung von Eingabedaten.
    pass
