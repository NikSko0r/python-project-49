import random
from brain_games.pattern_logic_brain import global_logic
from brain_games.cli import welcome_user


def expressions_logic_even():
    question = random.randint(1, 100)
    if question % 2 == 0:
        expression = 'yes'
    else:
        expression = 'no'
    return question, expression


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    flag = 1
    counter = 0
    while flag:
        question, expression = expressions_logic_even()
        flag = global_logic(question, expression)
        counter += flag    
        if counter == 3:
            print(f"Congratulations, {name}!")
            break
    if flag == 0:
        print(f"Let's try again, {name}!")