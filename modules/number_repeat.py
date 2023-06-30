import operator
import random
from modules.msg_print import *
from rich.console import Console
from config import config


def calc_number_repeat(amt, min, max, repeat):
    console = Console()
    numList = {}

    with console.status(config['PROGRESS_STATUS']) as status:
        # Create Dictionary
        rpt = range(min, max + 1)
        for i in rpt:
            numList[i] = 0

        # Pick a number
        for x in range(repeat):
            for y in range(amt):
                picked = random.randint(1, max)
                numList[picked] += 1

        # Sorting
        resultList = sorted(
            numList.items(), key=operator.itemgetter(1), reverse=True)

    display_repeat_count(resultList, amt)
    check_continue()
    return 0
