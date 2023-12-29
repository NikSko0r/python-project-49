from brain_games.cli import welcome_user
from brain_games.pattern_logic_brain import global_logic
import random
import math


def isprime(number):
    if number % 2 == 0:
        return False
    divider = 3
    while divider <= math.sqrt(number) and number % divider != 0:
        divider += 2
    return divider > math.sqrt(number)


def prime_expressions():
    number = random.randint(3, 200)
    if isprime(number):
        expression = "yes"
    else:
        expression = "no"
    return number, expression


def prime_calculate():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    flag = 1
    counter = 0
    while flag:
        question, expression = prime_expressions()
        flag = global_logic(question, expression)
        counter += flag
        if counter == 3:
            print(f"Congratulations, {name}!")
            break
    if flag == 0:
        print(f"Let's try again, {name}!")
