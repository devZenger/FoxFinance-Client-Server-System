import os
import json
import traceback
from datetime import datetime


first_log = False
# will set by config_logging_loader:
load_config_done = False

path_log_file = ""

print_errors_msg = True
print_status_msg = True
save_errors_msg = True
save_status_msg = True


def load_config():
    global path_log_file
    global print_errors_msg
    global print_status_msg
    global save_errors_msg
    global save_status_msg

    path_config = os.path.join("..", "server", "logger", "config.json")

    with open(path_config, "r") as config_data:
        config = json.load(config_data)

    date = datetime.now().strftime("%Y-%m-%d")

    filename = f"{config["filename"]}_{date}.txt"

    path_list: list = config["path"]
    path_list.append(filename)

    path_log_file = os.path.join(*path_list)

    print_errors_msg = config["print_errors_msg"]
    print_status_msg = config["print_status_msg"]
    save_errors_msg = config["save_errors_msg"]
    save_status_msg = config["save_status_msg"]


def format_Exception_e(e):
    error_message_list = []
    current_e = e
    space_depth = 0

    while current_e:
        space = "  " * space_depth
        error_message_list.append(f"{space}Fehlertyp: {type(current_e).__name__}")
        error_message_list.append(f"{space}Nachricht: {current_e}")
        error_message_list.append(f"{space}Traceback: ")

        tb = " ".join(traceback.format_tb(current_e.__traceback__))
        error_message_list.append(tb)

        current_e = current_e.__cause__
        if current_e:
            error_message_list.append(f"{space}Ursache: ")
        space_depth += 1

    error_message = "\n".join(error_message_list)

    return error_message


def message_to_log(message: str, m_type: str | None, print_head: bool = True):

    if load_config_done is False:
        try:
            load_config()
        except Exception as e:
            print("Logger-Konfigurationsdaten konnte nicht geladen.\n"
                  "Ort: message_to_log (logger.py)\n"
                  f"Error: {e}")

    global first_log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    length = 40

    if first_log is False:

        try:
            with open(path_log_file, "a") as logdatei:
                logdatei.write(
                    "\n\n"
                    f"{'=' * length}\n"
                    f"Logging gestartet um {timestamp}\n"
                    f"{'-' * length}")

        except Exception as e:
            print(f"Logger Datei konnte nicht erstellt werden, Fehler: {str(e)}")

        first_log = True

    if m_type == "error":
        head_title = "Fehlermeldung"
    elif m_type == "status":
        head_title = "Stausmeldung"
    elif m_type == "error_login":
        head_title = "Fehlerhafter Login-Versuch"
    else:
        head_title = "Unbekannt"

    if print_head:
        head = f"{head_title} - {timestamp}\n{'-' * length}"

    if print_errors_msg or print_status_msg:
        if print_head:
            print(head)
        print(message)

    try:
        if save_errors_msg is True or save_status_msg is True:
            with open(path_log_file, "a") as logdatei:
                if print_head:
                    logdatei.write(f"\n{head}")
                logdatei.write(f"\n{message}")
    except Exception as e:
        print(f"Logger konnte Fehlermeldung nicht speichern:\n"
              "Ort: message_to_log (logger.py)\n"
              f"Error: {str(e)}")


def error_message(e):
    error_message = format_Exception_e(e)
    message_to_log(error_message, "error", True)


def error_login_message(message: str):
    message_to_log(message, "login_error")


def status_message(message: str, print_head: bool = True):
    message_to_log(message, "status", print_head)


if __name__ == "__main__":

    status_message("Mit Datenbank verbunden")
    status_message("Aktien einfügen", False)
