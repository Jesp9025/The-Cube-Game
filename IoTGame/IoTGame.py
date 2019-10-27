import random

def start():
    print("########################################")
    print("Welcome to the IoT Game\nYou will be given a question about IoT(Internet of Things)\nThere will be a few possible answers to choose from")
    print("You only get 1 question, and 1 attempt to guess the correct answer.")
    print("The questions will be about Arduino, C language, and a some component questions.")
    print("Correct answer will deal 150 damage to the dragon\nIncorrect answer will regenerate 35 of dragons health")
    print("\nLets begin\n")

def iotGame():
    number = random.randint(1, 6) #Random number to know which question to get asked
    correctAns = 0 #placeholder for the correct answer for the questions
    global points #points is used to give/take points from the player when he finishes the game

    #Basically if number is 1, it will ask question no.1, if number is 2, it will ask question no.2 etc.
    #Uses a while loop to make use of 'try and except'. This prevents program from crashing if you type a non-int into the input
    while True:
        if number == 1:
            correctAns = 1
            try:
                answer = int(input("Is a mosfet voltage or current controlled?\n1: Voltage controlled\n2: Current controlled\nYour answer: "))
            except ValueError:
                print("########################################\nNot a number.\n########################################")
                continue
            if answer == correctAns:
                print("Correct.\nYou deal 150 damage to the dragon")
                points = -150
                break
            else:
                print("Wrong. The correct answer is", correctAns, "\nThe dragon regenerates 35 health")
                points = 35
                break
        elif number == 2:
            correctAns = 3
            try: 
                answer = int(input("How many analog levels does a 10-bit Arduino have?\n1: 2056\n2: 4096\n3: 1024\n4: 65536\nYour answer: "))
            except ValueError:
                print("########################################\nNot a number.\n########################################")
                continue
            if answer == correctAns:
                print("Correct.\nYou deal 150 damage to the dragon")
                points = -150
                break
            else:
                print("Wrong. The correct answer is", correctAns, "\nThe dragon regenerates 35 health")
                points = 35
                break
        elif number == 3:
            correctAns = 2
            try: 
                answer = int(input("How many analog levels does a 12-bit Arduino have?\n1: 2056\n2: 4096\n3: 1024\n4: 65536\nYour answer: "))
            except ValueError:
                print("########################################\nNot a number.\n########################################")
                continue
            if answer == correctAns:
                print("Correct.\nYou deal 150 damage to the dragon")
                points = -150
                break
            else:
                print("Wrong. The correct answer is", correctAns, "\nThe dragon regenerates 35 health")
                points = 35
                break
        elif number == 4:
            correctAns = 4
            try: 
                answer = int(input("How many analog levels does an 8-bit Arduino have?\n1: 2056\n2: 128\n3: 1024\n4: 256\nYour answer: "))
            except ValueError:
                print("########################################\nNot a number.\n########################################")
                continue
            if answer == correctAns:
                print("Correct.\nYou deal 150 damage to the dragon")
                points = -150
                break
            else:
                print("Wrong. The correct answer is", correctAns, "\nThe dragon regenerates 35 health")
                points = 35
                break
        elif number == 5:
            correctAns = 1
            try: 
                answer = int(input("In C programming, should you define functions() before or after the main() function?\n1: Before\n2: After\nYour answer: "))
            except ValueError:
                print("########################################\nNot a number.\n########################################")
                continue
            if answer == correctAns:
                print("Correct.\nYou deal 150 damage to the dragon")
                points = -150
                break
            else:
                print("Wrong. The correct answer is", correctAns, "\nThe dragon regenerates 35 health")
                points = 35
                break
        elif number == 6:
            correctAns = 2
            try: 
                answer = int(input("How do you define a function in C language?\n1: functionName()\n2: void functionName()\n3: functionName();\n4: void functionName();\nYour answer: "))
            except ValueError:
                print("########################################\nNot a number.\n########################################")
                continue
            if answer == correctAns:
                print("Correct.\nYou deal 150 damage to the dragon")
                points = -150
                break
            else:
                print("Wrong. The correct answer is", correctAns, "\nThe dragon regenerates 35 health")
                points = 35
                break
