import random
from rich.console import Console
from const import const
from ..utils.msg_print import *
from ..utils.error_check import *


def execute_number_shuffle():
    error_flg = False
    while True:
        if error_flg:
            clear_screen()
            err_panel(const['ERROR_INPUT'])
            error_flg = False

        amount_input = input(f"{const['REQUIRE_NUMBER_NEED']} : ")
        if not amount_input.isdigit():
            error_flg = True
            continue
        min_range_input = input(f"{const['REQUIRE_MINIMUM']} : ")
        if not min_range_input.isdigit():
            error_flg = True
            continue
        max_range_input = input(f"{const['REQUIRE_MAXIMUM']} : ")
        if not max_range_input.isdigit():
            error_flg = True
            continue
        shuffle_count_input = input(
            f"{const['REQUIRE_SHUFFLE_COUNT']} : ")
        if not shuffle_count_input.isdigit():
            error_flg = True
            continue

        if check_min_max(int(min_range_input), int(max_range_input)):
            if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                calc_number_shuffle(int(amount_input), int(min_range_input), int(
                    max_range_input), int(shuffle_count_input))
                break
        else:
            err_panel(const['ERROR_INPUT'])


def calc_number_shuffle(amt, min, max, shuffle):
    console = Console()
    numberList = list(range(min, max+1))

    with console.status(const['PROGRESS_STATUS']) as status:
        for _ in range(shuffle):
            random.shuffle(numberList)

    result_panel(str(numberList[:amt]))
    input(const['REQUIRE_CONTINUE'])
    clear_screen()
