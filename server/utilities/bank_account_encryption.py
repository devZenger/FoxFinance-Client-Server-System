from cryptography.fernet import Fernet
import base64
import os

_fernet = None


def read_bank_account_key():

    path = os.path.join("..", "server", "keys", "demo_account.key")
    try:
        with open(path, "rb") as key_file:
            secret_key = key_file.read()
        return secret_key
    except FileNotFoundError as e:
        error_msg = ("'demo_account.key' konnte nicht geöffnet werden.\n"
                     f"Pfad: {path}\n"
                     f"Error: {str(e)}\n")
        raise RuntimeError(error_msg) from e


def _get_fernet():
    global _fernet
    if _fernet is None:
        key = read_bank_account_key()
        _fernet = Fernet(key)
    return _fernet


def bank_account_encode(account: str):

    encode_byte = _get_fernet().encrypt(account.encode('utf-8'))
    encode_str = base64.urlsafe_b64encode(encode_byte).decode('utf-8')
    return encode_str


def bank_account_decode(encode: str):
    encode_byte = base64.urlsafe_b64decode(encode.encode('utf-8'))
    decode = _get_fernet().decrypt(encode_byte).decode('utf-8')

    return decode


if __name__ == "__main__":

    test = "test"

    answer = bank_account_encode(test)

    print(type(answer))
    print(answer)

    anser2 = bank_account_decode(answer)

    print(anser2)
