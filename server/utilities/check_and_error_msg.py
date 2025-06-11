from passlib.context import CryptContext
from datetime import datetime, timedelta

############################
# Overview:
# -------------------------
# Messages:
# 1. _error_msg 
# 2. error_msg_db_sql
# 3. error_msg_no_service
# 4. error_forwarding_msg
#
# Check-functions:
# 1. check_not_None
# 2. check_not_empty
# 3. check_not_None_and_empty
# 4. check_len_bg2
# 5. check_house_number
# 6. check_zip_code
# 7. check_time_format
# 8. check_birthday
# 9. check_email
# 10. check_phone_number
# 11. check_fin_amount
# 12. check_password
# 13. check_isin


# 1. _error_msg
_error_msg = (
    "\tWir bitten um Ihr Verständnis\n"
    "\tViele Grüsse, das FoxFinance Team"
    )

# 2. error_msg_db_sql
error_msg_db_sql = (
    "Es tut und leid, die Anfrage konnte nicht verarbeitet werden.\n"
    f"{_error_msg}"
    )

# 3. error_msg_no_service
error_msg_no_service = (
    "Es tut uns leid, ein unerwarteter Fehler ist aufgetreten.\n"
    "\tDer Service steht derzeit nicht zur Verfügung\n"
    f"{_error_msg}"
    )

# 4. error_forwarding_msg
error_forwarding_msg = "Weitergeleiteter Fehler aus einer tieferen Ebene"


# 1. check_not_None
def check_not_None(value):
    if value is None:
        raise ValueError("Ungültige Eingabe")


# 2. check_not_empty
def check_not_empty(value: str | dict | list):
    if isinstance(value, (str, dict, list)) and not value:
        raise ValueError("Ungültige Eingabe")


# 3. check_not_None_and_empty
def check_not_None_and_empty(value: str | dict | list):
    check_not_None(value)
    check_not_empty(value)


# 4. check_len_bg2
def check_len_bg2(value):
    if len(value) >= 2:
        return value
    else:
        raise ValueError("Keine gültige Eingabe")


# 5. check_house_number
def check_house_number(value):
    if not value:
        raise ValueError("Die Hausnummer darf nicht leer sein.")
    for v in value:
        if v.isdigit():
            return value
        else:
            raise ValueError("Die Hausnummer muss eine Zahl beinhalten")


# 6. check_zip_code
def check_zip_code(value: int):
    try:
        value = int(value)
        if value >= 1067 and value <= 99998:
            return value
        else:
            raise ValueError("ungültige Postleitzahl")

    except ValueError:
        raise ValueError("ungültige Postleitzahl")


# 7. check_time_format
def check_time_format(time: str):
    time = time.strip()
    try:
        split = time.split(".")
        if len(split[0]) == 2 and len(split[1]) == 2 and len(split[2]) == 4:
            return True
        else:
            raise ValueError("Bitte das Format tt.mm.jjjj beachten")

    except ValueError as e:
        raise ValueError("Bitte das Format tt.mm.jjjj beachten") from e


# 8. check_birthday
def check_birthday(value: str):
    test = check_time_format(value)
    if test:
        today = datetime.today()
        adult_date = today - timedelta(days=18*365)
        birthday = datetime.strptime(value, "%d.%m.%Y")
        if birthday <= adult_date:
            return value
        else:
            raise ValueError("unter 18")


# 9. check_email
def check_email(value: str):
    char_a = "@"
    char_dot = "."
    if char_a in value and char_dot in value:
        return value
    else:
        raise ValueError("Ungültige E-Mail Adressse.")


# 10. check_phone_number
def check_phone_number(value: str):
    if len(value) >= 11 and len(value) <= 13:
        for number in value:
            if not number.isdigit():
                raise ValueError("Telefonnummer darf nur Zahlen beinhalten.")

        return value

    else:
        raise ValueError("Ungülitge Länge.")


# 11. check_fin_amount
def check_fin_amount(value):
    try:
        value = float(value)
        if value >= 0:
            return value
        else:
            raise ValueError("Bitte eine positive Zahl eingeben.")
    except ValueError:
        raise ValueError("Bitte eine positive Zahl eingaben.")


# 12. check_password
def check_password(value: str):
    if len(value) >= 12:

        upper = 0
        lower = 0
        special = 0
        numbers = 0

        for char in value:
            if char.isupper() and char.isalpha():
                upper += 1
            elif char.islower() and char.isalpha():
                lower += 1
            elif char.isdigit():
                numbers += 1
            elif not char.isalnum():
                special += 1

        if upper > 1 and lower > 1 and numbers > 1 and special >= 1:

            password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            return password_context.hash(value)
        else:
            raise ValueError("Passwort entspricht nicht den Sicherheitsstandart.")
    else:
        raise ValueError("Mindestens zwölf Zeichen.")


# 13. check_isin
def check_isin(value: str):
    if len(value) != 12:
        raise ValueError("Ungültige ISIN, keine 12 Zeichen lang.")
    return value
