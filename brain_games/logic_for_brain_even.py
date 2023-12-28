import random
import brain_games.cli


def brain_even():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    flag = 1
    counter = 0
    while flag:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").lower()
        if number % 2 == 0 and answer == "yes" or number % 2 != 0 and answer == "no":
            counter += 1
            print("Correct!")
            if counter == 3:
                print(f"Congratulations, {name}!")
                break
            continue
        else:
            flag = 0
            correct_answer = "no" if number % 2 != 0 else "yes"
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
