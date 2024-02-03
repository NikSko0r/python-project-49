import random

from brain_games.consts import PROGR_INSTRUCTION, MIN_PROGR_LEN, MAX_PROGR_LEN
from brain_games.engine import run_game


def get_progr_and_miss_num():
    start, step = random.randint(1, 100), random.randint(1, 100)
    progr_length = random.randint(MIN_PROGR_LEN, MAX_PROGR_LEN)
    miss_index = random.randint(0, progr_length - 1)
    row_progr = ' '.join(
        ['..' if i == miss_index else str(start + step * i) for i in range(progr_length)])
    miss_num = start + step * miss_index
    return row_progr, str(miss_num)


def run_progr_game():
    run_game(get_progr_and_miss_num, PROGR_INSTRUCTION)
