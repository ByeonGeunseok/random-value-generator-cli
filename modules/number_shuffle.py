import random
from rich.console import Console
from conf import config
from modules.msg_print import *


def calc_number_shuffle(amt, min, max, shuffle):
    console = Console()
    numberList = list(range(min, max+1))

    with console.status(config['PROGRESS_STATUS']) as status:
        for _ in range(shuffle):
            random.shuffle(numberList)

    print(numberList[:amt])
    check_continue()
    return 0
