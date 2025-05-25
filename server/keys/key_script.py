import os
import secrets
from cryptography.fernet import Fernet


def generate_key(filename, key):
    path_list = ["..", "server", "keys"]
    path_list.append(filename)
    path = os.path.join(*path_list)
    print("path", path)
    with open(path, "wb") as key_file:
        key_file.write(key)


def create_keys():

    account_key = Fernet.generate_key()
    generate_key("demo_account.key", account_key)

    token_key_str = secrets.token_hex(32)
    token_key = token_key_str.encode("utf-8")
    generate_key("demo_token.key", token_key)

    return ("Neue Schlüssel für Bankkonto und Token wurden erstellt.\n")


if __name__ == "__main__":
    print("aktuelles verzeichnis", os.getcwd())
    create_keys()
    print("Beide Schlüssel erfolgreich erstellt")
