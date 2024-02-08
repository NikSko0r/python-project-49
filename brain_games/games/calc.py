import random
import operator


def get_question_and_answer():
    instruction = 'What is the result of the expression?'
    math_signs = ('+', '-', '*')
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(math_signs)
    if math_sign == '+':
        answer = operator.add(num1, num2)
    elif math_sign == '*':
        answer = operator.mul(num1, num2)
    elif math_sign == '-':
        answer = operator.sub(num1, num2)
    question = f'{num1} {math_sign} {num2}'
    return question, str(answer), instruction
