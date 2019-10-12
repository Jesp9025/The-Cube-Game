#Dont mind this. Just playing around with the merging of the codes
import random, time

totalPoints = 0
pointsToWin = 5
gameName = ""

def countdown(): #Countdown to start game
    print("The game is gonna be", gameName)
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")
    time.sleep(1)

def randomNum(): #Chooses a random game
    global randomGame
    randomGame = random.randint(1,2)

while True: #Runs until you reach the required points
    if totalPoints >= pointsToWin:
        print("YOU WON!!")
        break
    randomNum()

    #Guess a number-game
    if randomGame == 1:
        gameName = "Guess a number-Game"
        countdown()

        number = random.randint(1,10)
        attempts = 3
        print("########################################")
        print("Welcome to the Number-Guessing-Game\nYou have 3 attempts to guess the correct number.\nThe number is generated randomly from 1 to 10")
        print("########################################")

        while True: #This will make the code run until it reaches a break
            try: #try and except is used to prevent program from crashing if you enter a non-int as input
                answer = int(input("Guess the number: ")) #User types a number
                if answer >= 1 and answer <= 10: #If answer is higher than or equal to 1, and less than or equal to 10, do the code
                    attempts -= 1
                    if answer == number: #If user guesses the correct number
                        print("You guessed the correct number!\nYou get 1 point.")
                        totalPoints += 1
                        break
                    elif attempts <= 0: #If user runs out of attempts
                        print("You ran out of attempts.\nThe correct answer is", number, "\nYou lose 1 point.")
                        totalPoints -= 1
                        break
                    elif answer > number: #Tells the user to try a lower number
                        print("Try a lower number")
                    elif answer < number: #Tells the user to try a higher number
                        print("Try a higher number")
                else: #This will happen if guessed number is lower than 1, or higher than 10
                    print("You can't guess a number lower than 1 or higher than 10. We won't count this as an attempt.")
            except ValueError: #This will make sure the program doesn't crash in case we get a ValueError. ValueError occours when you try to type non-int into input(string,float)
                print("That was not a valid number. We won't count this as an attempt.")
                continue
        continue

    #Math game
    if randomGame == 2:
        gameName = "Math Game"
        countdown()

        ops = ['+', '-', '*']                                   #adds the options for the equations
        rand=random.randint(1,100)                              #chooses a number between 1 and 100
        rand2=random.randint(1,100)                             #chooses a number between 1 and 100
        operation = random.choice(ops)                          #chooses a random equation from the line before
        maths = eval(str(rand) + operation + str(rand2))        #does the actual equation
        print ("Your question is",rand,operation,rand2)         #tells the user what the equation is
        d=int(input ("What is your answer:"))                   #asks the user for the awnser
        if d==maths:                                            #checks if the input is the same as the awnser
            print ("Correct, you may move to the next room")  
            totalPoints += 1                                    #output if the awnser is correct
        else:
            print ("Incorrect. The actual answer is",maths) 
            totalPoints -= 1                                    #output if the awnser is wrong, and tells the right awnser
