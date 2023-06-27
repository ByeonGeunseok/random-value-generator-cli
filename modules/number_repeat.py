import operator
import random
import time
from modules.msg_print import *


def number_repeat(amt, min, max, repeat):
    numList = {}

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

    amount = range(0, amt)
    for z in amount:
        print(resultList[z])

    return 0
