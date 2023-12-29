from brain_games.cli import welcome_user
from brain_games.pattern_logic_brain import global_logic
import random


def find_progressions():
    first_number = random.randint(1, 50)
    step_progression = random.randint(1, 20)
    list_progression = [
        first_number + step_progression * i for i in range(1, random.randint(5, 15))
    ]
    number_change = random.randint(0, len(list_progression) - 1)
    list_progression_copy = list_progression[:]
    expression = list_progression_copy[number_change]
    list_progression[number_change] = ".."
    for i in range(len(list_progression)):
        list_progression[i] = str(list_progression[i])
    question = " ".join(list_progression)
    return question, str(expression)


def progressions_calculate():
    name = welcome_user()
    print("What number is missing in the progression?")
    flag = 1
    counter = 0
    while flag:
        question, expression = find_progressions()
        flag = global_logic(question, expression)
        counter += flag
        if counter == 3:
            print(f"Congratulations, {name}!")
            break
    if flag == 0:
        print(f"Let's try again, {name}!")
