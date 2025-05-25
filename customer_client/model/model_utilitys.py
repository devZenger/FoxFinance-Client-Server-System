from datetime import datetime, timedelta


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


def time_format_check_de(time: str):
    time = time.strip()
    try:
        split = time.split(".")

        if 3 > len(split[0]) > 0 and 3 > len(split[1]) > 0 and len(split[2]) == 4:
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


def age_check(birthday: str):
    today = datetime.today()
    adult_date = today - timedelta(days=18*365)

    birthday_obj = datetime.strptime(birthday, "%d.%m.%Y")
    if birthday_obj <= adult_date:
        return True
    else:
        return False


def change_date_format(date: str):

    date_split = date.split(".")

    for i in range(2):
        if len(date_split[i]) < 2:
            date_split[i] = f"0{date_split[i]}"

    print(f"len0 {len(date_split[0])} len1 {len(date_split[1])} len2 {len(date_split[2])}")
    if len(date_split[0]) == 2 and len(date_split[1]) == 2 and len(date_split[2]) == 4:
        new_date = f"{date_split[2]}-{date_split[1]}-{date_split[0]}"
    else:
        print(f"fehler {date_split[2]}, date_split 1 {date_split[1]}, {date_split[0]}")

    return new_date


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


def check_date_input(input, change: bool = True):
    check_en = time_format_check_en(input)
    check_de = time_format_check_de(input)
    if check_en:
        return True, input, ""
    elif check_de == check_date(input):
        check_real = check_date(input)
        if check_real:
            if not change:
                return True, input, ""
            else:
                date = change_date_format(input)
                print(date)
                return True, date, ""
        else:
            return False, "Ungültiges Datum"
    else:
        return False, None, "Eingabeformat muss tt.mm.jjjj entsprechen"
