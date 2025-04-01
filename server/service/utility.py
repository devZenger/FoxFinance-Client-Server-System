def date_form_validation(input: str):

    date_arry = input.split("-")

    if len(date_arry[0]) == 4 and len(date_arry[1]) == 2 and len(date_arry[2]) == 2:
        return True

    else:
        raise ValueError("ungültiges Datum")
