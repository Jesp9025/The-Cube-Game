import random, time
import GuessingGame, MathGame, hangman, SubnettingGame, PythonGame, IoTGame
import subprocess, platform

#-------------------------------------------------------------------------
#The dragons health, task at hand of the game, and difficulty choosing
#-------------------------------------------------------------------------

easyMode = 0
normalMode = 0
hardMode = 0
totalHealth = 0
healthToWin = 0

#Function to clear the terminal
#https://stackoverflow.com/questions/2084508/clear-terminal-in-python 
def clearTerminal():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else: #Linux and Mac
        print("\033c", end="")

while True:
    print("\nBefore anything happens, please choose the difficulty")
    gameDifficulty = input("Type in \"Easy\", \"Normal\" or \"Hard\": ").upper()
    if gameDifficulty == "EASY":
        easyMode += 1
        totalHealth += 1000
        break
    elif gameDifficulty == "NORMAL":
        normalMode += 1
        totalHealth += 1500
        break
    elif gameDifficulty == "HARD":
        hardMode += 1
        totalHealth += 2000
        print("*The game whispers: \"A daring one, are we?\"*")
        break
    else:
        print("\nPlease input a proper difficulty")

#------------------------------------------------------------------------
#The countdown that starts every mini game
#------------------------------------------------------------------------

def countdown(n=3):
  print("Starting in...")
  time.sleep(1)
  while n > 0:
    print(n, end="\r")
    n -= 1
    time.sleep(1)

#------------------------------------------------------------------------
#The very start of the game
#------------------------------------------------------------------------

def startingMsg():
    global masterName
    print("\n\nWelcome to this mini-story text adventure game")
    print("created by a small group of unqualified people")
    masterName = input("Currently, we'd like you to input a name of your choice: ")
    time.sleep(1)
    print("\nThank you for your cooperation, and we hope that you enjoy this game")
    time.sleep(2)
    countdown()
    clearTerminal()
    
startingMsg()

#-------------------------------------------------------------------------
#The game's story
#-------------------------------------------------------------------------

def startingStory():
    print("\n\nOnce upon a time, in a totally normal world, in a totally normal house")
    time.sleep(3)
    print("An adventurous soul lived, and that soul was the human named " + masterName, ".\n")
    time.sleep(3)
    print("One day you started thriving to find an adventure you could complete.")
    time.sleep(3)
    print("Luckily for you, a dungeon was found recently by the townsfolk.")
    time.sleep(3)
    print("A few days pass, and you hear a rumour, that the dungeon is impossible to complete.")
    time.sleep(3)
    print("This makes you even more intrigued, and so on, you decide to explore")
    time.sleep(3)
    print("The so called ")
    time.sleep(2)
    print("01000100")
    print("01110101")
    print("01101110")
    print("01100111")
    print("01100101")
    print("01101111")
    print("01101110")
    time.sleep(3)
    print("\nAfter getting your gear, you set off towards the dungeon.\n")
    time.sleep(3)
    print("A day passes and after some weak mob killing, you notice")
    time.sleep(3)
    print("A huge weird entrance. You immediately think: ")
    time.sleep(3)
    print("\"It must be the boss room\", and without a second thought, ")
    time.sleep(3)
    print("You enter the said room.")
    time.sleep(3)
    print("\nSome time pass and all of the torches lit up.")
    time.sleep(3)
    print("You look around and in the middle of the room ")
    time.sleep(3)
    print("You see a dragon, snoozing calmly.")
    time.sleep(3)
    print("Quietly, you approach the dragon, hoping to make a decisive blow without a fight.")
    time.sleep(3)
    print("Unfortunately, the dragon wakes up after you take a few steps.")
    time.sleep(3)
    print("Raging because it's sleep was disturbed, it emerges itself into fighting you.")
    time.sleep(3)
    print("Without any other option, you prepare yourself for an intense battle!")
    time.sleep(4)


startingStory()
#-------------------------------------------------------------------------
#Instructions of the game
#-------------------------------------------------------------------------
def instructions():
    print("\nSo the point of the game as you should have guessed by now")
    time.sleep(2)
    print("Is of course to slay the dragon")
    time.sleep(2)
    print("\nThe game goes like this: You complete the mini-games ")
    time.sleep(2)
    print("You deal damage to the dragon")
    time.sleep(2)
    print("\nDifferent games deal different amount of damage")
    time.sleep(2)
    print("If you answer incorrectly, the dragon regenerates some of it's life")
    time.sleep(2)
    answer = input("\nWith that said, are you ready?: ").upper()
    if answer == "YES" or answer == "Y":
        print("Good luck with your adventure!")
    elif answer == "NO" or answer == "N":
        print("Well goodbye then! We'll see you on a different adventure")
        exit()
    time.sleep(2)
    clearTerminal()


instructions()
#-------------------------------------------------------------------------
#The story after winning the game
#-------------------------------------------------------------------------
def endingStory():
    print("As you take your last hit to defeat the dragon, you notice something")
    time.sleep(3)
    print("The dragon starts glitching right before your eyes, and then just disappears into thin air")
    time.sleep(3)
    print("You keep staring into nothingness for a bit, thinking of what just happened")
    time.sleep(3)
    print("But without coming to a conclusion, you just decide to not overthink, and go home")
    time.sleep(3)
    print("\nSadenned, by the fact that you were not able to get any loot from the dragon,")
    time.sleep(3)
    print("You go home with a happy face, knowing that you can brag about how you completed")
    time.sleep(3)
    print("The so called \"impossible\" to complete dungeon all by yourself!")
    
#-------------------------------------------------------------------------
#Random game chooser
#-------------------------------------------------------------------------

def randomNum():
    global randomGame
    randomGame = random.randint(1,6)

randomNum()
#-------------------------------------------------------------------------
#A loop that runs until you defeat the dragon
#-------------------------------------------------------------------------

while True:
    if totalHealth < healthToWin:
        time.sleep(2)
        endingStory()
        time.sleep(3)
        print ("\n\nWith that said, the unqualified people were happy that you played the game")
        time.sleep(3)
        print ("So here's one last question")
        time.sleep(2)
        playAgain = input("\nWould you Like to play the game again?: ").upper()
        if playAgain == "YES" or playAgain == "Y":
            clearTerminal()
            if easyMode == 1:
                totalHealth = 1000
                print("The game has been reset")
                print("Health set to", totalHealth)
                time.sleep(2)
            elif normalMode == 1:
                totalHealth = 1500
                print("The game has been reset")
                print("Health set to", totalHealth)
                time.sleep(2)
            elif hardMode == 1:
                totalHealth == 2000
                print("The game has been reset")
                print("Health set to", totalHealth)
                time.sleep(2)
        elif playAgain == "NO" or playAgain == "N":
            print("Thank you for playing the game!")
            exit()
        else:
            print("We would like to get a \"Yes\" or a \"No\" as an answer")
    elif totalHealth > healthToWin:
        randomNum()


#-------------------------------------------------------------------------
#Game chooser based on the random number generated
#-------------------------------------------------------------------------

    if randomGame == 1:
        gameName = "Guess a number-Game"
        print("The game you'll be playing right now is...", gameName)
        countdown()
        clearTerminal()
        GuessingGame.start()
        GuessingGame.game()
        totalHealth = totalHealth + GuessingGame.points
        print("\nDragons remaining health:", totalHealth, "\n")
        time.sleep(2)
    elif randomGame == 2:
        gameName = "Math game"
        print("The game you'll be playing right now is...", gameName)
        countdown()
        clearTerminal()
        MathGame.start()
        MathGame.mathFunc()
        totalHealth = totalHealth + MathGame.points
        print("\nDragons remaining health:", totalHealth, "\n")
        time.sleep(2)
    elif randomGame == 3:
        gameName = "Hangman"
        print("The game you'll be playing right now is...", gameName)
        countdown()
        clearTerminal()
        hangman.initialize()
        hangman.start()
        hangman.secret()
        hangman.game()
        totalHealth = totalHealth + hangman.points
        print("\nDragons remaining health:", totalHealth, "\n")
        time.sleep(2)
    elif randomGame == 4:
        gameName = "Subnetting game"
        print("The game you'll be playing right now is...", gameName)
        countdown()
        clearTerminal()
        SubnettingGame.start()
        SubnettingGame.subnetGame()
        totalHealth = totalHealth + SubnettingGame.points
        print("\nDragons remaining health:", totalHealth, "\n")
        time.sleep(2)
    elif randomGame == 5:
        gameName = "IoT game"
        print("The game you'll be playing right now is...", gameName)
        countdown()
        clearTerminal()
        IoTGame.start()
        IoTGame.iotGame()
        totalHealth = totalHealth + IoTGame.points
        print("\nDragons remaining health:", totalHealth, "\n")
        time.sleep(2)
    elif randomGame == 6:
        gameName = "Python game"
        print("The game you'll be playing right now is...", gameName)
        countdown()
        clearTerminal()
        PythonGame.start()
        PythonGame.questionFunc()
        PythonGame.pythonGame()
        totalHealth = totalHealth + PythonGame.points
        print("\nDragons remaining health:", totalHealth, "\n")
        time.sleep(2)