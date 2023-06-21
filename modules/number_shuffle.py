import random


def number_shuffle(amt, min, max, shuffle):
    numberList = list(range(min, max+1))

    for sfl in range(shuffle):
        random.shuffle(numberList)

    print(numberList[:amt])

    return 0

# number_shuffle(amount_input, min_range_input,
#                max_range_input, shuffle_count_input)
