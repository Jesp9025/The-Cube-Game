""" Python Mini-Game by Julius Pazitka Team 3 
Inspiration for working with classes (OOP)
https://www.mikedane.com/programming-languages/python/building-a-quiz/
Inspiration from another example of the game
https://stackoverflow.com/questions/26792705/how-to-create-a-simple-quiz-in-python-with-multiple-topics
"""

import random

# Welcome Message
def start():
  print("########################################"
      "\nHello, welcome to The Python Quiz Mini Game"
      "\nIn this quiz, you will be asked 10 questions about programming language - Python."
      "\nTry your best to answer all 10 correctly." 
      "\nEnter 1, 2, 3, 4 or 5 for answer"
      "\nDepending on which answer you think is right"
      "\nEach correct answer will deal 10 damage to the dragon"
      "\nAnd incorrect will regenerate 5 health\n")


class Quiz:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.q = question
    self.cA = correctAnswer
    self.oA = otherAnswers

# List of questions
def questionFunc():
  global questionList
  questionList = [Quiz("A comment in Python language can start with # sign. (True or false)", "True", ["False"]),
  Quiz("What is the correct file extension for Python files?", ".py", [".pt", ".pyth", ".pyt", ".pptx"]),
  Quiz("How do you create a variable with the floating number 2.8?", "Both the other answers are correct", ["x = float(2.8)", "x = 2.8"]),
  Quiz("Which operator is used to multiply numbers?", "*", ["/", "#", "%"]),
  Quiz("Which operator can be used to compare two values?", "==", ["<>", "><", "="]),
  Quiz("What is the correct syntax to output the type of a variable or object in Python?", "print(type(x))", ["print(typeof x)", "print(typeOf(x)", "print(typeof(x))"]),
  Quiz("Which statement is used to stop a loop?", "break", ["stop", "exit", "return"]),
  Quiz("Python is an interpreted language. (True or false)", "true", ["false"]),
  Quiz("The continue command is used to exit a loop. (True or false)", "false", ["true"]),
  Quiz("Which method can be used to remove any whitespace from both the beginning and the end of a string?", "strip()", ["len()", "trim()", "ptrim()"])
  ]
  random.shuffle(questionList)

def pythonGame():
  global points
  score = 0
  regen = 0
  for questionIndex in questionList:
    print(questionIndex.q)
    print("Possible answers are:")
    possible = questionIndex.oA + [questionIndex.cA] # square brackets turn correct answer into list for concatenating with other list
    random.shuffle(possible)
    count = 0 # list indexes start at 0 in python

    while count < len(possible):
      print(str(count+1) + ": " + possible[count])
      count += 1
    print("Please enter the number of your answer:")
    print("↓")

    playerAnswer = input()

    while not playerAnswer.isdigit():
      print("That was not a number. Please enter the number of your answer:")
      playerAnswer = input()
    playerAnswer = int(playerAnswer)

    while not (playerAnswer > 0 and playerAnswer <= len(possible)):
      print("That number doesn't correspond to any answer. Please enter the number of your answer:")
      playerAnswer = input()

    if possible[playerAnswer-1] == questionIndex.cA:
      print("Your answer was correct.")
      score += 1

    else:
      print("Your answer was wrong.")
      print("Correct answer was: " + questionIndex.cA)
      regen += 5
    print("")

  print("You answered " + str(score) + " of " + str(len(questionList)) + " questions correctly.")
  print("Final score is:", score, "out of", len(questionList), "that is", float(score / len(questionList)) * 100, "%")
  damage = score * 10
  points = score * (-10) + regen
  print("You deal", damage, "damage to the dragon, and it regenerates", regen, "health")