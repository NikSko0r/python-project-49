import random

from brain_games.consts import PROGR_INSTRUCTION, MIN_PROGR_LEN, MAX_PROGR_LEN
from brain_games.engine import run_game


def get_progr_and_miss_num():
    start, step = random.randint(1, 100), random.randint(1, 100)
    row_len = random.randint(MIN_PROGR_LEN, MAX_PROGR_LEN)
    miss = random.randint(0, row_len - 1)  # index
    row_progr = ' '.join(
        ['..' if i == miss else str(start + step * i) for i in range(row_len)])
    miss_num = start + step * miss
    return row_progr, str(miss_num)


def run_progr_game():
    run_game(get_progr_and_miss_num, PROGR_INSTRUCTION)
