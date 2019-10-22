# Prototype

questions = ["In Python, you can define a variable without specifying its data type?",
             "The print function is used to receive data from keyboard in a program.",
             "A comment in Python language can start with # sign.",
             "13/4 = 3.25 Is this the right result?"
            ]
answer_choices = ["a)True\nb)False\n:",
                  "a)True\nb)False\n:",
                  "a)True\nb)False\n:",
                  "a)True\nb)False\n:",
                ]
correct_choices = [{"a", "True"},
                   {"b", "False"},
                   {"a", "True"},
                   {"a", "True"},]
answers = ["Yes, you can.",
           "The print() function prints the specified message to the screen, or other standard output device.",
           ":",
           "The result is 3.25",
           ]

def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

if __name__ == "__main__":
    quiz()
