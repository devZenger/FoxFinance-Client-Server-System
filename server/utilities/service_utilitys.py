def date_form_validation(input: str):

    date_arry = input.split("-")

    if len(date_arry[0]) == 4 and len(date_arry[1]) == 2 and len(date_arry[2]) == 2:
        print("date vali erfolgreich")
        return True

    else:
        raise False


def time_check(time: str):
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
