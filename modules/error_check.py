def check_min_max(min, max):
    if min <= 0:
        print("Minimum number must bigger than 0.")
        return False
    if max <= 0:
        print("Minimum number must bigger than 0.")
        return False
    if min >= max:
        print("Minimum number must bigger than Maximum.")
        return False
    return True


def check_is_number(*args):
    is_number = True
    for i in args:
        if type(i) is not int:
            if i.isdigit():
                is_number = True
            else:
                is_number = False
                break
    if is_number:
        return True
    else:
        return False
