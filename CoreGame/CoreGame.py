#If we are to do this way, which is quite simple, all the minigames we make, has to be inside of a function so we can call it
#All python files has to be in the same folder for this to work
#It chooses a random game, problem is that it can choose the same game 2 times in a row
import random, time
import GuessingGame, MathGame #Imports the other python files

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
        GuessingGame.guessNum() #Here we call the function called guessNum from GuessingGame.py
    #Math Game   
    if randomGame == 2:
        gameName = "Math game"
        countdown()
        MathGame.mathFunc() #And here we call the mathFunc from MathGame.py
