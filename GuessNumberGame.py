import random

totalPoints = 0
number = random.randint(1,10)
attempts = 3
print("########################################")
print("Welcome to the Number-Guessing-Game\nYou have 3 attempts to guess the correct number.\nThe number is generated randomly from 1 to 10")
print("########################################")
while True:
    try:
        attempts -= 1
        answer = int(input("Guess the number: "))
        if answer <= 0:
            print("Can't be less than 1. We won't count this as an attempt.")
            attempts += 1
            continue
        elif answer >= 11:
            print("Can't be higher than 10. We won't count this as an attempt.")
            attempts += 1
        elif answer == number:
            print("You guessed the correct number!\nYou get 1 point.")
            totalPoints += 1
            print("Total points: ", totalPoints)
            break
        elif attempts <= 0:
            print("You ran out of attempts.\nYou lose 1 point.")
            totalPoints -= 1
            print("Total points: ", totalPoints)
            break
        elif answer > number:
            print("Lower")
        elif answer < number:
            print("Higher")
    except ValueError:
        print("That was not a number. We won't count this as an attempt.")
        attempts += 1
        continue
