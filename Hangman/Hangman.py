import random
import sys

#Had to put the initialization variables into a function, because if hangman was chosen again, it would mess with the whole thing, put double words, use same word etc.
#global is used so we can pull the variables from inside this function, to other functions.
def initialize():
    global randomWords
    global guess_word
    global randomizer
    global length_word
    global alphabet
    global letter_storage
    #Change the words whenever you want into whatever you like
    randomWords = ["among", "amount", "amusement", "brain", "change", "conscious",
                "curve", "design"]
    guess_word = []
    randomizer = random.choice (randomWords)
    length_word = len(randomizer)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_storage = []

#--------------------------------------------------------------------------------
#Basic introduction to the game

def start():
    print("########################################")
    print("Welcome to the Hangman game!\n")
    print("In this game you'll have 10 tries to guess the secret given word\n")
    print("Winning the game will deal 75 damage to the dragon\nLosing will regenerate 15 of the dragons health")

#--------------------------------------------------------------------------------
#The player is given with a choice if he wants to continue playing or if he wants to quit


def ready():
    print ("Well then, are you ready to play the game? (type 'yes' or 'no').\n")

    while True:
        choice = input().upper()

        if choice == "YES" or choice == "Y":
            break
        elif choice == "NO" or choice == "N":
            sys.exit(print("I guess you were too afraid to guess some words, see ya then!"))
            
        else:
            print ("We just told you to enter 'Yes' or 'No' for crying out loud.")

#-------------------------------------------------------------------------------
#Making the letters turn to "_"

def secret():

        for character in randomizer:
            guess_word.append("_")

        print("So the given word has", length_word, "letters")
        
        print("Remember that you can enter only 1 letter at a time\n\n")

        print(guess_word)

#-------------------------------------------------------------------------------
#The game itself

def game():

    global points #points is used to give/take points from the player when a game is finished
    guess_taken = 1
    while guess_taken < 10:

        guess = input("Pick a letter.\n").lower()


        #Checking if the input was a valid letter
        if not guess in alphabet:
            print("Please input a valid letter from the a-z alphabet.")
            
        #Checking if the letter was already used
        elif guess in letter_storage:
            print("You already tried this letter.\n\n")

        #Checking if the input letter was a correct letter from the secret word    
        else:
            letter_storage.append(guess)
            if guess in randomizer:
                print("That's one less letter to guess.\n\n")
                
                #And this prints the correct letter instead of '_'
                for x in range(0, length_word):
                    if randomizer[x] == guess:
                        guess_word[x] = guess
                        print (guess_word)
                        
                #If there aren't any shown symbols left, the game is won and it exits
                if not '_' in guess_word:
                    print("Congratulations, you may go to the next mini game.")
                    points = -75
                    
                    break
                
            #But if there are letters that have not been guessed before the lives ran out, the game exits without winning
            else:
                print("The letter you tried was incorrect. Have another go.\n\n")
                guess_taken += 1
                if guess_taken == 10:
                    print("Looks like you've failed. The secret word was", randomizer,  ". Better luck next time.")
                    points = 15
                    


#-------------------------------------------------------------------------------

#Regarding the main game, if you want to make the program continue after the "Hangman" was won, just
#insert the "if no '_' in guess_word:" command right after the "secret()" and "game()" functions

#And insert "else:" after that if the game was not won"





#This was mostly copied from "https://codereview.stackexchange.com/questions/178312/another-python-hangman"
#Just the variable names, function names and strings were modified, with the addition of deeper explanations than the original code.
#It was copied mainly because there are a lot of different Hangmans made out there, and whatever I would have wrote by
#Myself, it wouldn't have felt genuine anyways.
#I chose this one to copy because it was easy to understand, for me at least (Mantas)

