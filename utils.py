import os
from random import randint


def clear(): return os.system('clear')  # Clears the console window


def roll_dice(sides):
    return randint(1, sides)


def calculate_damage(attacker, defender):
    return (attacker + roll_dice(8)) - (defender + roll_dice(6))
