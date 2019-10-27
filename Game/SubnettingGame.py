import random

def start():
    print("########################################")
    print("Welcome to the subnetting game.\nHere you will get a question regarding subnetting. You have 1 attempt to guess the correct answer.\nThere will be 4 possible answers.")
    print("You will need to type the number of the answer you think is correct.")
    print("We prepared a little calculator if you need some help\n")
    print("Correct answer will deal 150 damage to the dragon\nIncorrect answer will regenerate 35 of dragons health")

def subnetGame():
    number = random.randint(1, 8) #Random number to know which question to get asked
    correctAns = 0 #placeholder for the correct answer for the questions
    global points #points is used to give/take points from the player when he finishes the game

    #Basically if number is 1, it will ask question no.1, if number is 2, it will ask question no.2 etc.
    #Uses a while loop to make use of 'try and except'. This prevents program from crashing if you type a non-int into the input
    while True:
        if number == 1:
            correctAns = 3
            try:
                answer = int(input("Enter the broadcast address for the network 172.20.218.128/25\n1: 172.20.218.224\n2: 172.20.218.248\n3: 172.20.218.255\n4: 172.20.218.0\nYour answer: "))
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
            correctAns = 2
            try:
                answer = int(input("Enter the broadcast address for the network 10.184.0.0/16\n1: 10.184.255.252\n2: 10.184.255.255\n3: 10.184.255.224\n4: 10.184.255.240\nYour answer: "))
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
                answer = int(input("What subnet mask would you use for the 172.29.0.0 network, such that you can get 2370 subnets and 10 hosts per subnet?\n1: 255.255.255.0\n2: 255.255.255.240\n3: 255.255.255.224\n4: 255.255.0.0\nYour answer: "))
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
                answer = int(input("What is the Subnet Mask corresponding to a shorthand of /20?\n1: 255.255.255.0\n2: 255.255.224.0\n3: 255.255.0.0\n4: 255.255.240.0\nYour answer: "))
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
                answer = int(input("What is the Subnet Mask corresponding to a shorthand of /29?\n1: 255.255.255.248\n2: 255.255.255.224\n3: 255.255.255.240\n4: 255.255.255.0\nYour answer: "))
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
            correctAns = 1
            try:
                answer = int(input("What subnet mask would you use for the 172.28.0.0 network, such that you can get 40 subnets and 730 hosts per subnet?\n1: 255.255.252.0\n2: 255.255.224.0\n3: 255.255.255.0\n4: 255.255.240.0\nYour answer: "))
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

        elif number == 7:
            correctAns = 2
            try:
                answer = int(input("Enter the first valid host on the network 172.17.0.0 255.255.0.0\n1: 172.17.0.0\n2: 172.17.0.1\n3: 172.17.0.16\n4: 172.17.0.128\nYour answer: "))
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

        elif number == 8:
            correctAns = 3
            try:
                answer = int(input("Enter the first valid host on the network 10.71.0.0/16\n1: 10.71.0.0\n2: 10.71.0.129\n3: 10.71.0.1\n4: 10.71.0.17\nYour answer: "))
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