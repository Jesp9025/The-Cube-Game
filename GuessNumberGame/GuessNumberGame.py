import random

def start():
    print("########################################")
    print("Welcome to the Number-Guessing-Game\nYou have 3 attempts to guess the correct number.\nThe number is generated randomly from 1 to 10")
    print("Winning the game will deal 120 damage to the dragon\nLosing the game will regenerate 25 of dragons health\n")
    
def game():
    number = random.randint(1,10)
    attempts = 3
    global points #points is used to give/take points from the player when he finishes the game
    while True: #This will make the code run until it reaches a break
        try: #try and except is used to prevent program from crashing if you enter a non-int as input
            answer = int(input("Guess the number: ")) #User types a number
            if answer >= 1 and answer <= 10: #If answer is higher than or equal to 1, and less than or equal to 10, do the code
                attempts -= 1
                if answer == number: #If user guesses the correct number
                    print("You guessed the correct number!\nThe dragon takes 120 damage")
                    points = -120
                    break
                elif attempts <= 0: #If user runs out of attempts
                    print("You ran out of attempts.\nThe correct answer is", number, "\nThe dragon regenerates 25 health")
                    points = 25
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
