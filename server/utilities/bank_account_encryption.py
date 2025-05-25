from cryptography.fernet import Fernet
import os
# SECRET_KEY = "5R-BaPrBgz5Rw97JhLRdAE5blwm2F-lIF_eZYCyDED0="
fernet = None


def read_key():
    global fernet
    path = os.path.join("..", "server", "keys", "demo_account.key")
    try:
        with open(path, "rb") as key_file:
            secret_key = key_file.read()

        fernet = Fernet(secret_key)

    except FileNotFoundError as e:
        error_msg = ("'demo_account.key' konnte nicht geöffnet werden.\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e


def bank_account_encode(account: str):
    if fernet is None:
        raise RuntimeError("Fernet wurd nicht initialisiert")

    encode = fernet.encrypt(account.encode('utf-8'))
    return encode


def bank_account_decode(encode):
    if fernet is None:
        raise RuntimeError("Fernet wurd nicht initialisiert")
    decode = fernet.decrypt(encode).decode('utf-8')
    return decode
