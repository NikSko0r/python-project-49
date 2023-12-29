def global_logic(
    question, exp
):  # exp = expression
    print(f"Question: {question}")
    answer = input("Your answer: ").lower()
    if exp == answer:
        print("Correct!")
        return 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{exp}'.")
        return 0
