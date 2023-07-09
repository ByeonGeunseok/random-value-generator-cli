from modules.msg_print import *
from const import const


def check_min_max(min: int, max: int):
    """
    Check minimum and maximum.\n
    1. Check if the minimum value is greater than 0.\n
    2. Check if the maximum value is greater than 0.\n
    3. Check if maximum value is equal to or greater than minimum value.\n
    Return True, If all conditions are satisfied.
    """
    if min < 0:
        err_panel(const['ERROR_MIN_ZERO'])
        return False
    if max < 0:
        err_panel(const['ERROR_MAX_ZERO'])
        return False
    if min >= max:
        err_panel(const['ERROR_NUMBER_COMPARE'])
        return False
    return True


def check_range_cnt(amount: int, min: int, max: int) -> bool:
    """
    Check if the number of elements between minimum value and maximum value is less than the desired quantity.
    """
    range_cnt = 0
    for _ in range(min, max + 1):
        range_cnt += 1

    if range_cnt < amount:
        return False
    else:
        return True
