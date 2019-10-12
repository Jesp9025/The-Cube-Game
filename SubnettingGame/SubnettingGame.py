import random

number = random.randint(1, 5) #Random number to know which question to get asked
correctAns = 0 #placeholder for the correct answer for the questions
print("#######################################################")
print("Welcome to the subnetting game.\nHere you will get a question regarding subnetting. You have 1 attempt to guess the correct answer.\nThere will be 4 possible answers.")
print("You will need to type the number of the answer you think is correct.")
print("We prepared a little calculator if you need some help")
print("#######################################################")
#Basically if number is 1, it will ask question no.1, if number is 2, it will ask question no.2 etc.
if number == 1:
    correctAns = 3
    answer = int(input("Enter the broadcast address for the network 172.20.218.128/25\n1: 172.20.218.224\n2: 172.20.218.248\n3: 172.20.218.255\n4: 172.20.218.0\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 2:
    correctAns = 2
    answer = int(input("Enter the broadcast address for the network 10.184.0.0/16\n1: 10.184.255.252\n2: 10.184.255.255\n3: 10.184.255.224\n4: 10.184.255.240\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 3:
    correctAns = 2
    answer = int(input("What subnet mask would you use for the 172.29.0.0 network, such that you can get 2370 subnets and 10 hosts per subnet?\n1: 255.255.255.0\n2: 255.255.255.240\n3: 255.255.255.224\n4: 255.255.0.0\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 4:
    correctAns = 4
    answer = int(input("What is the Subnet Mask corresponding to a shorthand of /20?\n1: 255.255.255.0\n2: 255.255.224.0\n3: 255.255.0.0\n4: 255.255.240.0\Your answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 5:
    correctAns = 1
    answer = int(input("What is the Subnet Mask corresponding to a shorthand of /29?\n1: 255.255.255.248\n2: 255.255.255.224\n3: 255.255.255.240\n4: 255.255.255.0\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 6:
    correctAns = 1
    answer = int(input("What subnet mask would you use for the 172.28.0.0 network, such that you can get 40 subnets and 730 hosts per subnet?\1: 255.255.252.0\n2: 255.255.224.0\n3: 255.255.255.0\4: 255.255.240.0\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 7:
    correctAns = 2
    answer = int(input("Enter the first valid host on the network 172.17.0.0 255.255.0.0\n1: 172.17.0.0\n2: 172.17.0.1\n3: 172.17.0.16\n4: 172.17.0.128\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
elif number == 8:
    correctAns = 3
    answer = int(input("Enter the first valid host on the network 10.71.0.0/16\n1: 10.71.0.0\n2: 10.71.0.16\n3: 10.71.0.1\n4: 10.71.0.16\nYour answer: "))
    if answer == correctAns:
        print("Correct.\nYou get 1 point.")
    else:
        print("Wrong.\nYou lose 1 point.")
