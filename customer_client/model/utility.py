from datetime import datetime, timedelta


def time_check(time: str):
    time = time.strip()
    try:
        split = time.split("-")
        if len(split[0]) == 4 and len(split[1]) == 2 and len(split[2]) == 2:
            return True
        else:
            return False

    except AttributeError:
        return False
    except IndexError:
        return False


def time_check_two(time: str):
    time = time.strip()
    try:
        split = time.split(".")
        if len(split[0]) == 2 and len(split[1]) == 2 and len(split[2]) == 4:
            return True
        else:
            return False

    except AttributeError:
        return False
    except IndexError:
        return False


def email_check(email: str):
    email = email.strip()
    char_a = "@"
    char_dot = "."
    if char_a in email and char_dot in email:
        return True
    else:
        False


def password_check(password: str):

    upper = 0
    lower = 0
    special = 0
    numbers = 0

    for char in password:
        if char.isupper() and char.isalpha():
            upper += 1
        elif char.islower() and char.isalpha():
            lower += 1
        elif char.isdigit():
            numbers += 1
        elif not char.isalnum():
            special += 1

    if upper < 1:
        return False, "ein Großbuchstabe"
    elif lower < 1:
        return False, "ein Kleinbuchstabe"
    elif numbers < 1:
        return False, "eine Zahl"
    elif special < 1:
        return False, "ein Sonderzeichen"
    else:
        return True, ""


def house_number_check(house_number: str):

    for house in house_number:
        if house.isdigit():
            return True
    return False


def phone_number_check(phone_number: str):

    for phone in phone_number:
        if not phone.isdigit():
            return False
    return True


def age_check(birthday: str):
    today = datetime.today()
    adult_date = today - timedelta(years=18)

    birthday_obj = datetime.strptime(birthday, "%d.%.%Y")
    if birthday_obj <= adult_date:
        return True
    else:
        return False
