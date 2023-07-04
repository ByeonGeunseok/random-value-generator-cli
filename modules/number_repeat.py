import operator
import random
from modules.msg_print import *
from modules.error_check import *
from rich.console import Console
from const import const


def execute_number_repeat():
    amount_input = input(f"{const['REQUIRE_NUMBER_NEED']} : ")
    min_range_input = input(f"{const['REQUIRE_MINIMUM']} : ")
    max_range_input = input(f"{const['REQUIRE_MAXIMUM']} : ")
    repeat_count_input = input(f"{const['REQUIRE_REPEAT_COUNT']} : ")

    # If all inputs are numeric
    if check_is_number(amount_input, min_range_input, max_range_input, repeat_count_input):
        if check_min_max(int(min_range_input), int(max_range_input)):
            if check_range_cnt(int(amount_input), int(min_range_input), int(max_range_input)):
                calc_number_repeat(int(amount_input), int(min_range_input), int(
                    max_range_input), int(repeat_count_input))
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
    check_continue()
    return 0
