import random

def start():
    print("Welcome to the Math game."
        "\nYou will get a random math question"
        "\nCorrect answer will deal 50 damage to the dragon"
        "\nIncorrect answer will regenerate 15 health to the dragon")

def mathFunc():
    global points #points is used to give/take points from the player when he finishes the game
    ops = ['+', '-', '*'] #adds the options for the equations
    rand=random.randint(1,100) #chooses a number between 1 and 100
    rand2=random.randint(1,100) #chooses a number between 1 and 100
    operation = random.choice(ops) #chooses a random equation from the line before
    maths = eval(str(rand) + operation + str(rand2)) #does the actual equation
    print ("Your question is",rand,operation,rand2) #tells the user what the equation is
    d=int(input ("What is your answer: ")) #asks the user for the awnser
    if d==maths: #checks if the input is the same as the awnser
        print ("Correct, you may move to the next room") #output if the awnser is correct
        points = -50
    else:
        print ("Incorrect. The actual answer is",maths) #output if the awnser is wrong, and tells the right awnser
        points = 15