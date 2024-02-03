import random
import math

from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import run_game


def get_pair_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    pair = f'{num1} {num2}'
    result = math.gcd(num1, num2)
    return pair, str(result)


def run_gcd_game():
    run_game(get_pair_and_result, GCD_INSTRUCTION)
