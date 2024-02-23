import random


INSTRUCTION = "What number is missing in the progression?"


def get_question_and_answer():
    min_progres_len = 5
    max_progres_len = 10
    start, step = random.randint(1, 100), random.randint(1, 100)
    row_len = random.randint(min_progres_len, max_progres_len)
    miss_index = random.randint(0, row_len - 1)  # index
    finish = start + (step * row_len)
    answer = start + step * miss_index
    questions = [
        str(number) if number != answer else ".."
        for number in range(start, finish, step)
    ]
    question = " ".join(questions)
    return question, str(answer)
