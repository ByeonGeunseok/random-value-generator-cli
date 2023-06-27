import random
import time


def number_shuffle(amt, min, max, shuffle):
    numberList = list(range(min, max+1))

    for sfl in range(shuffle):
        random.shuffle(numberList)

    print(numberList[:amt])

    return 0
