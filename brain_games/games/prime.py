import random

from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_num_and_result():
    num = random.randint(1, 100)
    result = 'yes' if is_prime(num) else 'no'
    return num, result


def run_prime_game():
    run_game(get_num_and_result, PRIME_INSTRUCTION)
