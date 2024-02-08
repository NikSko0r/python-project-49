import random


def get_question_and_answer():
    instruction = 'What number is missing in the progression?'
    min_progres_len = 5
    max_progres_len = 10
    start, step = random.randint(1, 100), random.randint(1, 100)
    row_len = random.randint(min_progres_len, max_progres_len)
    miss = random.randint(0, row_len - 1)  # index
    question = ' '.join(
        ['..' if i == miss else str(start + step * i) for i in range(row_len)])
    answer = start + step * miss
    return question, str(answer), instruction
