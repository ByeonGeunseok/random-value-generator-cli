import random
from rich.console import Console
from message import message
from ..utils.msg_print import *
from ..utils.error_check import *


def execute_number_shuffle():
    error_flg = False
    while True:
        if error_flg:
            clear_screen()
            err_panel(message['ERROR_INPUT'])
            error_flg = False
        # Number amount
        amount_input = input(
            f"{message['REQUIRE_NUMBER_NEED']} ({message['QUIT_MESSAGE']}): ")
        if amount_input == '!q':
            break
        if not amount_input.isdigit():
            error_flg = True
            continue
        # Minimum number range
        min_range_input = input(
            f"{message['REQUIRE_MINIMUM']} ({message['QUIT_MESSAGE']}): ")
        if min_range_input == '!q':
            break
        if not min_range_input.isdigit():
            error_flg = True
            continue
        # Maximum number range
        max_range_input = input(
            f"{message['REQUIRE_MAXIMUM']} ({message['QUIT_MESSAGE']}): ")
        if max_range_input == '!q':
            break
        if not max_range_input.isdigit():
            error_flg = True
            continue
        # Shuffle count
        shuffle_count_input = input(
            f"{message['REQUIRE_SHUFFLE_COUNT']} ({message['QUIT_MESSAGE']}): ")
        if shuffle_count_input == '!q':
            break
        if not shuffle_count_input.isdigit():
            error_flg = True
            continue

        if check_min_max(int(min_range_input), int(max_range_input)):
            if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                calc_number_shuffle(int(amount_input), int(min_range_input), int(
                    max_range_input), int(shuffle_count_input))
                break
        else:
            err_panel(message['ERROR_INPUT'])


def calc_number_shuffle(amt, min, max, shuffle):
    is_calc = True

    while True:
        if is_calc:
            console = Console()
            numberList = list(range(min, max+1))

            with console.status(message['PROGRESS_STATUS']) as status:
                for _ in range(shuffle):
                    random.shuffle(numberList)

            result_panel(str(numberList[:amt]))
        try_input = input(message['REQUIRE_AGAIN'] + ' ' + '(y/n) >>')

        match try_input:
            case "y":
                clear_screen()
                is_calc = True
                continue
            case "n":
                clear_screen()
                break
            case _:
                is_calc = False
                continue
