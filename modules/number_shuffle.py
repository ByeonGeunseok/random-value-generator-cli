import random
import time


def number_shuffle(amt, min, max, shuffle):
    # Time start
    start_time = time.time()

    numberList = list(range(min, max+1))

    for sfl in range(shuffle):
        random.shuffle(numberList)

    print(numberList[:amt])

    # Time End
    end_time = time.time()

    print(end_time - start_time)
    return 0
