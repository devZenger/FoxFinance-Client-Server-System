import os
import sys
from fastapi import FastAPI
import uvicorn

from logger import status_message, error_message
from database import update_stock_datas, create_db
from keys import create_keys
from service import get_token_key
from utilities import DBOperationError, StockDataFetchError, read_bank_account_key
import utilities.config_loader

from api import (depot_apis,
                 depot_trade_and_transfer_apis,
                 registration_and_auth_apis,
                 information_api)

server = FastAPI()

server.include_router(depot_apis.router)
server.include_router(registration_and_auth_apis.router)
server.include_router(depot_trade_and_transfer_apis.router)
server.include_router(information_api.router)


@server.get("/")
async def root():
    return {"message": "Willkommen bei Fox Finance Service"}


def start_server(server_config: dict):
    status_message("Start Server.\nKonfiguration:\n"
                   f"Host: {server_config["host"]}\n"
                   f"Port: {server_config["port"]}\n"
                   f"Log Level: {server_config["log_level_uvicorn"]}\n"
                   f"Reload: {server_config["reload"]}\n")
    uvicorn.run(
        "main_server:server",
        host=server_config["host"],
        port=server_config["port"],
        log_level=server_config["log_level_uvicorn"],
        reload=server_config["reload"])


def end_main_server():
    status_message("\nProgramm wurde beendet.\n")
    sys.exit(0)


if __name__ == "__main__":

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    launch = True
    count = 0
    option = True
    user_input = ""

    while launch:
        utilities.config_loader.load_config()
        path_db = utilities.config_loader.path_db
        server_config = utilities.config_loader.server_config

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
                    end_main_server()

                case _:
                    print("Eingabe konnte nicht zugordnet werden, bitte wiederholen.")
                    count += 1
                    if count > 3:
                        end_main_server()
    try:
        update_stock_datas()
    except (StockDataFetchError, DBOperationError, Exception) as e:
        error_msg = ("Fehler bei Aufruf der Funktion: update_stock_datas.\n"
                     "Ort: main_server.py\n"
                     f"Error: {str(e)}\n")
        error_message(e, error_msg)
        end_main_server()

    # load key
    def key_error(name: str, e):
        error_msg = f"{name}-Schlüssel konnte nicht gelesen werden."
        error_message(e, error_msg)
        end_main_server()

    try:
        key = read_bank_account_key()
        if key is None:
            raise ValueError("Bankkonte-Schlüssel ist None")
    except Exception as e:
        error_msg = key_error("Bankkonto")
        error_message(e, error_msg)
        end_main_server()
    try:
        key = get_token_key()
        if key is None:
            raise ValueError("Token Schlüssel ist None")
    except Exception as e:
        error_msg = ("Token", e)
        error_message(e, error_msg)

    try:
        start_server(server_config)
    except Exception as e:
        error_msg = ("Fehler führte zum Beenden des Programms."
                     "Ort: main_server.py\n"
                     f"Error: {str(e)}")
        error_message(e, error_msg)
        end_main_server()
