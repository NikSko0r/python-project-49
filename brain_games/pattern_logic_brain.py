def global_logic(question, expression):    #name_game includes text, question, expression (optional)
        print(f"Question: {question}")
        answer = input("Your answer: ").lower()
        if expression == answer:
            print("Correct!")
            return 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{expression}'."
            )
            return 0