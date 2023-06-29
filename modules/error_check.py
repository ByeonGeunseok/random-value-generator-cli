from modules.msg_print import *
from config import config


def check_min_max(min, max):
    if min < 0:
        err_panel(config['ERROR_MIN_ZERO'])
        return False
    if max < 0:
        err_panel(config['ERROR_MAX_ZERO'])
        return False
    if min >= max:
        err_panel(config['ERROR_NUMBER_COMPARE'])
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
