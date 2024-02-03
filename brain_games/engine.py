import prompt
from brain_games.consts import AMOUNT_OF_ROUNDS


def run_game(get_question_and_result, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{instruction}')
    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_result = get_question_and_result()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_result}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
