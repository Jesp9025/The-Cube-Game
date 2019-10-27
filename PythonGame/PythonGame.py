""" 
Python Mini-Game by Julius Pazitka Team 3 
Inspiration for working with classes (OOP)
https://www.mikedane.com/programming-languages/python/building-a-quiz/
Inspiration from another example of the game
https://stackoverflow.com/questions/26792705/how-to-create-a-simple-quiz-in-python-with-multiple-topics

Introduction to Python MiniGame

Its a simple text-based quiz game with options (from 2 to 5). Only one option is correct. The quiz has 10 questions.

After the quiz, terminal show your result. The options are in numerical order.

"""

import random # We need this to randomly arrange the possible answers.

# Welcome Message
# Print a message onto the startup screen:
print("\nHello, welcome to The Python Quiz Mini Game"
      "\nIn this quiz, you will be asked 10 questions about programming language - Python."
      "\nTry your best to answer all 10 correctly." 
      "\nEnter 1, 2, 3, 4 or 5 for answer"
      "\nDepending on which answer you think is right\n")

""" 
We define Quiz class. This class will consist of a question and 2 types of answers:
1., Correct answer
2., Another group of other (incorrect) answers

The __init__() function will be called whenever you create a new object in quizList with the function Quiz(), 
with its arguments being passed on into the correct attribute.

Self represents the instance of the class (for example in this code, represents the instance of the questions, 
correct answers and other incorrect answers.)
By using the “self” keyword we can access the attributes and methods of the class.
"""
class Quiz:
  def __init__(self, question, correctAnswer, otherAnswers): 
    self.q = question
    self.cA = correctAnswer
    self.oA = otherAnswers

# List of questions
# Format of the question: Question, correct answer, other incorrect answers
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

score = 0 # Variable that counts how many answers were correct. Always beginning from zero. 
random.shuffle(questionList) # this function always displays questions in a random order

# Main loop. The program loop should go over each item of the list
for questionIndex in questionList:
  print(questionIndex.q) # Output each question.
  print("Possible answers are:") # Output for possible answer
  """
  All possible answers should appear in a random order so that the correct answer isn't always at the same position. 
  For example: always on the first position
  All options is in random order with numbers. Every option has own number of the answer.

  """
  possible = questionIndex.oA + [questionIndex.cA] # square brackets turn correct answer into list for connection with other list
  random.shuffle(possible) 
  count = 0 # list indexes start at 0, counts from 0 

# Players input (interaction with player)
# While loop is checking whether what the user entered is really a number that corresponds with an answer.
# If the player has entered something other than the answer number, the game will notify him

  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  print("↓") # Cursor

  playerAnswer = input()

  while not playerAnswer.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    playerAnswer = input()
  playerAnswer = int(playerAnswer)

  while not (playerAnswer > 0 and playerAnswer <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    playerAnswer = input()

# Checking the correct answers

# The condition compares the player's response with the correct answer
# If they are the same, the user's answer was correct and the variable score should be increased by 1 (+ 1 point). 
# Else, it's wrong and the user should be told the correct answer. 

  if possible[playerAnswer-1] == questionIndex.cA:
    print("Your answer was correct.")
    score += 1

  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + questionIndex.cA)
  print("")

# Result of the player
print("You answered " + str(score) + " of " + str(len(questionList)) + " questions correctly.") # The len() function returns the number of correct items in questionList.
print("Final score is:", score, "out of", len(questionList), "that is", float(score / len(questionList)) * 100, "%") # Score in percentage (float)
input("Press any key for exit")