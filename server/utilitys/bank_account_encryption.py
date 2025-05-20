from cryptography.fernet import Fernet

SECRET_KEY = "5R-BaPrBgz5Rw97JhLRdAE5blwm2F-lIF_eZYCyDED0="


def bank_account_encode(account: str):
    fernet = Fernet(SECRET_KEY)
    encode = fernet.encrypt(account.encode('utf-8'))
    return encode


def bank_account_decode(encode):
    fernet = Fernet(SECRET_KEY)
    decode = fernet.decrypt(encode).decode('utf-8')
    return decode
