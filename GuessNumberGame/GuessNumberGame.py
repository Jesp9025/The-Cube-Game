import random

totalPoints = 0
number = random.randint(1,10)
attempts = 3
print("########################################")
print("Welcome to the Number-Guessing-Game\nYou have 3 attempts to guess the correct number.\nThe number is generated randomly from 1 to 10")
print("########################################")
while True:
    try:
        answer = int(input("Guess the number: "))
        
        if answer >= 1 and answer <= 10:
            attempts -= 1
            if answer == number:
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
                print("Try a lower number")
            elif answer < number:
                print("Try a higher number")
        else:
            print("You can't guess a number lower than 1 or higher than 10. We won't count this as an attempt.")
    except ValueError:
        print("That was not a number. We won't count this as an attempt.")
        continue
