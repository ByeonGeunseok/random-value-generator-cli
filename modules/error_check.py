def check_min_max(min, max):
    if min <= 0:
        print("Minimum number must bigger than 0.")
        return 0
    if max <= 0:
        print("Minimum number must bigger than 0.")
        return 0
    if min >= max:
        print("Minimum number must bigger than Maximum.")
        return 0
    return 1
