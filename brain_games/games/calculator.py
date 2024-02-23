import random
import operator


INSTRUCTION = 'What is the result of the expression?'


def get_question_and_answer():
    signs_and_operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(signs_and_operators)
    question = f'{num1} {math_sign[0]} {num2}'
    answer = math_sign[1](num1, num2)
    return question, str(answer)
