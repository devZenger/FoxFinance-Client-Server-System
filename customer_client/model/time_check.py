

def time_check(time: str):

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
