#########################
# 1. time_format_check_en
# 2. time_format_check_de
# 3. check_date
# 4. check_date_input
# 5. format_time_to_de
# 6. format_time_to_en
# 7. check_email

# 1.
def time_format_check_en(time: str):
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


# 2.
def time_format_check_de(time: str):
    time = time.strip()
    try:
        split = time.split(".")

        if 3 > len(split[0]) > 0 and 3 > len(split[1]) > 0 and len(split[2]) == 4:
            day = f"{split[0].rjust(2, "0")}"
            month = f"{split[1].rjust(2, "0")}"
            return True, f"{day}.{month}.{split[2]}"
        else:
            return False, ""

    except AttributeError:
        return False, ""
    except IndexError:
        return False, ""


# 3.
def check_date(date: str):
    # format dd.mm.yyyy
    d_split = date.split('.')

    day = int(d_split[0])
    month = int(d_split[1])
    year = int(d_split[2])
    test = False

    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if 1 <= day <= 29:
                test = True
        if 1 <= day <= 29:
            test = True

    elif month % 2 == 0 and 2 < month < 13:
        if 1 <= day <= 30:
            test = True

    elif month % 2 != 0 and 0 < month < 12:
        if 1 <= day <= 31:
            test = True
    else:
        test = False

    if test is True:
        return True
    else:
        return False


# 4.
def check_date_input(input: str):
    check_de = False
    check_en = False
    check_en = time_format_check_en(input)
    check_de, date = time_format_check_de(input)
    if check_en:
        return True, input, "EN"
    elif check_de:
        check_real = check_date(date)
        if check_real:
            return True, date, ""
        else:
            return False, "Ungültiges Datum"
    else:
        return False, None, "Eingabeformat muss tt.mm.jjjj entsprechen"


# 5.
def format_time_to_de(value: str) -> str:

    v = value.split("-")

    return f"{v[2]}.{v[1]}.{v[0]}"


# 6.
def format_time_to_en(value: str) -> str:

    v = value.split(".")
    return f"{v[2]}-{v[1]}-{v[0]}"


# 7.
def check_email(email: str):
    email = email.strip()
    char_a = "@"
    char_dot = "."
    if char_a in email and char_dot in email:
        return True
    else:
        False
