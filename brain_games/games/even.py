import random

from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game


def is_even(num):
    return num % 2 == 0


def get_even_and_result():
    num = random.randint(1, 100)
    result = 'yes' if is_even(num) else 'no'
    return num, result


def run_even_game():
    run_game(get_even_and_result, EVEN_INSTRUCTION)
