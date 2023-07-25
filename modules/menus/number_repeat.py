import operator
import random
from ..utils.msg_print import *
from ..utils.error_check import *
from rich.console import Console
from const import const


def execute_number_repeat():
    error_flg = False
    while True:
        if error_flg:
            clear_screen()
            err_panel(const['ERROR_INPUT'])
            error_flg = False
        # Number amount
        amount_input = input(
            f"{const['REQUIRE_NUMBER_NEED']} ({const['QUIT_MESSAGE']}): ")
        if amount_input == '!q':
            break
        if not amount_input.isdigit():
            error_flg = True
            continue
        # Minimum number range
        min_range_input = input(
            f"{const['REQUIRE_MINIMUM']} ({const['QUIT_MESSAGE']}): ")
        if min_range_input == '!q':
            break
        if not min_range_input.isdigit():
            error_flg = True
            continue
        # Maximum number range
        max_range_input = input(
            f"{const['REQUIRE_MAXIMUM']} ({const['QUIT_MESSAGE']}): ")
        if max_range_input == '!q':
            break
        if not max_range_input.isdigit():
            error_flg = True
            continue
        # Repeat Count
        repeat_count_input = input(
            f"{const['REQUIRE_REPEAT_COUNT']} ({const['QUIT_MESSAGE']}): ")
        if repeat_count_input == '!q':
            break
        if not repeat_count_input.isdigit():
            error_flg = True
            continue

        if check_min_max(int(min_range_input), int(max_range_input)):
            if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                calc_number_repeat(int(amount_input), int(min_range_input), int(
                    max_range_input), int(repeat_count_input))
                break
        else:
            err_panel(const['ERROR_INPUT'])


def calc_number_repeat(amt, min, max, repeat):
    console = Console()
    numList = {}

    with console.status(const['PROGRESS_STATUS']) as status:
        # Create Dictionary
        rpt = range(min, max + 1)
        for i in rpt:
            numList[i] = 0

        # Pick a number
        for x in range(repeat):
            for y in range(amt):
                picked = random.randint(min, max)
                numList[picked] += 1

        # Sorting
        resultList = sorted(
            numList.items(), key=operator.itemgetter(1), reverse=True)

    display_repeat_count(resultList, amt)
    input(const['REQUIRE_CONTINUE'])
    clear_screen()
