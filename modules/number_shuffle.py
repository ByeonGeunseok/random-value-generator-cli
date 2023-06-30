import random
from rich.console import Console
from config import config


def calc_number_shuffle(amt, min, max, shuffle):
    console = Console()
    numberList = list(range(min, max+1))

    with console.status(config['PROGRESS_STATUS']) as status:
        for _ in range(shuffle):
            random.shuffle(numberList)

    print(numberList[:amt])

    return 0
