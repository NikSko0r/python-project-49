from brain_games.cli import welcome_user
from brain_games.pattern_logic_brain import global_logic
import random


def gcd_divisor(first_number, second_number):
    if first_number > second_number:
        temp = second_number
    else:
        temp = second_number
    gcd = 1
    for i in range(1, temp + 1):
        if first_number % i == 0 and second_number % i == 0:
            gcd = i
    return gcd


def gcd_expressions():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f"{first_number} {second_number}"
    expression = gcd_divisor(first_number, second_number)
    return question, str(expression)


def gcd_calculation():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    flag = 1
    counter = 0
    while flag:
        question, expression = gcd_expressions()
        flag = global_logic(question, expression)
        counter += flag
        if counter == 3:
            print(f"Congratulations, {name}!")
            break
    if flag == 0:
        print(f"Let's try again, {name}!")
