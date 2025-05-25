import os
import sys
from fastapi import FastAPI
import uvicorn

from logger import status_message, error_message
from database import update_stock_datas, create_db
from keys import create_keys
from utilities import DBOperationError, StockDataFetchError
import utilities.config_loader

from api import (depot_stock_apis,
                 depot_overview_apis,
                 depot_financial_apis,
                 depot_settings_api,
                 authentication_apis,
                 create_customer_accout_api,
                 information_api)

server = FastAPI()

server.include_router(create_customer_accout_api.router)
server.include_router(authentication_apis.router)
server.include_router(depot_overview_apis.router)
server.include_router(information_api.router)
server.include_router(depot_stock_apis.router)
server.include_router(depot_financial_apis.router)
server.include_router(depot_settings_api.router)


@server.get("/")
async def root():
    return {"message": "Willkommen bei Fox Finance Service"}


def start_server():
    status_message("Start Server")
    uvicorn.run(
        "main_server:server",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True)


if __name__ == "__main__":

    launch = True
    count = 0
    option = True
    user_input = ""

    while launch:
        utilities.config_loader.load_config()
        path_db = utilities.config_loader.path_db

        if os.path.exists(path_db):
            status_message("Datenbank vorhanden")
            launch = False

        else:
            if option:
                print("Keine Datenbank vorhanden.\n"
                      f"Pfad: {path_db}\n"
                      "Optionen:\n"
                      "1. Datenbank unter den angegeben Pfad erzeugen.\n"
                      "2. Nochmal überprüfen.\n"
                      "3. Serverprogramm beenden.\n")
                user_input = input("Bitte Menüpunkt auswählen (1, 2, 3): ")
                print(user_input)

            match user_input:

                case "1":
                    option = False
                    keys = False
                    user_input2 = input("Neue Schlüssel ebenfalls erstellen? (ja/nein): ")
                    user_input2 = user_input2.lower()
                    if user_input2 == "ja" or user_input2 == "j":
                        message = create_keys()
                        keys = True
                        status_message(message)
                    elif user_input2 == "nein" or user_input2 == "n":
                        keys = True
                    else:
                        keys = False
                    if keys:
                        message, email, password = create_db(path_db)
                        if email != "" and password != "":
                            message_st = (f"{message}\n"
                                          f"Max Mustermann erstellt.\n"
                                          f"Email: {email}\n"
                                          f"Passwort: {email}\n")
                        else:
                            message_st = message
                        status_message(message_st)
                        launch = False

                case "2":
                    pass

                case "3":
                    sys.exit(0)

                case _:
                    print("Eingabe konnte nicht zugordnet werden, bitte wiederholen.")
                    count += 1
                    if count > 3:
                        print("System wird beendet")
                        sys.exit(0)
    try:
        update_stock_datas()
    except StockDataFetchError as e:
        error_msg = ("Fehler bei Aufruf der Funktion: update_stock_datas.\n"
                     "Ort: main_server.py\n"
                     f"Error: {str(e)}\n")
        error_message(error_msg)
        raise StockDataFetchError(error_msg) from e
    except DBOperationError as e:
        error_msg = ("Fehler bei Aufruf der Funktion: update_stock_datas.\n"
                     "Ort: main_server.py\n"
                     f"Error: {str(e)}\n")
        error_message(error_msg)
        raise DBOperationError(error_msg) from e
    except Exception as e:
        error_msg = ("Fehler bei Aufruf der Funktion: update_stock_datas.\n"
                     "Ort: main_server.py\n"
                     f"Error: {str(e)}\n")
        error_message(error_msg)
        raise Exception(error_msg) from e
    start_server()
