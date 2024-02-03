import random

from brain_games.consts import MATH_SIGNS, CALC_INSTRUCTION
from brain_games.engine import run_game


def get_expression_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(MATH_SIGNS)
    expression = f'{num1} {math_sign} {num2}'
    result = eval(expression)
    return expression, str(result)


def run_calc_game():
    run_game(get_expression_and_result, CALC_INSTRUCTION)
