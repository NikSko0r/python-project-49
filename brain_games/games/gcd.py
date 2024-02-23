import random
import math


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    question = f'{num1} {num2}'
    answer = math.gcd(num1, num2)
    return question, str(answer)
