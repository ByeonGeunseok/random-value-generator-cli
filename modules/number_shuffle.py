import random
from rich.console import Console
from const import const
from modules.msg_print import *


def calc_number_shuffle(amt, min, max, shuffle):
    console = Console()
    numberList = list(range(min, max+1))

    with console.status(const['PROGRESS_STATUS']) as status:
        for _ in range(shuffle):
            random.shuffle(numberList)

    print(numberList[:amt])
    check_continue()
    return 0
