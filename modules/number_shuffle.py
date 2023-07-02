import random
from rich.console import Console
from const import const
from modules.msg_print import *
from modules.error_check import *


def execute_number_shuffle():
    amount_input = input(f"{const['REQUIRE_NUMBER_NEED']} : ")
    min_range_input = input(f"{const['REQUIRE_MINIMUM']} : ")
    max_range_input = input(f"{const['REQUIRE_MAXIMUM']} : ")
    shuffle_count_input = input(
        f"{const['REQUIRE_SHUFFLE_COUNT']} : ")

    # If all inputs are numeric
    if check_is_number(amount_input, min_range_input, max_range_input, shuffle_count_input):
        if check_min_max(int(min_range_input), int(max_range_input)):
            if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                calc_number_shuffle(int(amount_input), int(min_range_input), int(
                    max_range_input), int(shuffle_count_input))
    else:
        err_panel(const['ERROR_INPUT'])


def calc_number_shuffle(amt, min, max, shuffle):
    console = Console()
    numberList = list(range(min, max+1))

    with console.status(const['PROGRESS_STATUS']) as status:
        for _ in range(shuffle):
            random.shuffle(numberList)

    result_panel(str(numberList[:amt]))
    check_continue()
    return 0
