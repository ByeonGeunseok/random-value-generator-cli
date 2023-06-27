import random
import time
from rich.console import Console


def number_shuffle(amt, min, max, shuffle):
    console = Console()
    numberList = list(range(min, max+1))

    with console.status("[bold green]Working on tasks...") as status:
        for _ in range(shuffle):
            random.shuffle(numberList)

    print(numberList[:amt])

    return 0
