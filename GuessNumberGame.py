import random

totalPoints = 0 #Temporary placeholder for total points throughout the game
number = random.randint(1,10)
attempts = 3

print("########################################")
print("Welcome to the Number-Guessing-Game\nYou have 3 attempts to guess the correct number.\nThe number is generated randomly from 1 to 10")
print("########################################")

while True:
    attempts -= 1
    answer = int(input("Guess the number: "))
    if answer == number:
        print("You guessed the correct number!\nYou get 1 point.")
        totalPoints += 1
        print("Total points: ", totalPoints)
        break
    elif attempts == 0:
        print("You ran out of attempts.\nYou lose 1 point.")
        totalPoints -= 1
        print("Total points: ", totalPoints)
        break
    elif answer > number:
        print("Lower")
    elif answer < number:
        print("Higher")
