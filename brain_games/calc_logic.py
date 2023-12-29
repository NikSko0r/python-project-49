from brain_games.cli import welcome_user
from brain_games.pattern_logic_brain import global_logic
import random


def expressions_logic_calc():
    operator_list = ["+", "-", "*"]
    random_operator = random.choice(operator_list)
    first_number = random.randint(1, 50)
    second_number = random.randint(1, 50)
    question = f"{first_number} {random_operator} {second_number}"
    if random_operator == "+":
        expression = first_number + second_number
    elif random_operator == "-":
        expression = first_number - second_number
    elif random_operator == "*":
        expression = first_number * second_number
    return question, str(expression)


def calculator():
    name = welcome_user()
    print("What is the result of the expression?")
    flag = 1
    counter = 0
    while flag:
        question, expression = expressions_logic_calc()
        flag = global_logic(question, expression)
        counter += flag
        if counter == 3:
            print(f"Congratulations, {name}!")
            break
    if flag == 0:
        print(f"Let's try again, {name}!")
