

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
