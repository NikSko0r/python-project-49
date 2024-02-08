import prompt


def run_game(module):
    amount_of_rounds = 3
    _, _, instruction = module.get_question_and_answer()
    name = prompt.string(
        'Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(f'{instruction}')
    for _ in range(amount_of_rounds):
        question, correct_answer, _ = module.get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
