#
# Date: 1/17/19
# Author: Kyle Matheney
#
# https://exercism.io/my/solutions/e4a10fb0b5e742a2a98fab28440ae7cc

import random


def roll():
    return random.randint(1, 6)  # Rolls a 6-sided die


def get_largest(rolls):
    rolls.sort()  # Sorts rolls by ascending numerical value
    rolls.pop(0)  # Removes smallest value from list


def record_rolls():
    rolls = []

    for i in range(4):  # Rolls dice 4 times and records the result
        rolls.append(roll())
        # print(rolls[i])  # LINE TESTS THAT THE ARRAY IS FILLED CORRECTLY
    get_largest(rolls)


record_rolls()
