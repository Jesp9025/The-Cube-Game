import random
import time

ops = ['+', '-', '*']
rand=random.randint(1,100)
rand2=random.randint(1,100)
operation = random.choice(ops)
maths = eval(str(rand) + operation + str(rand2))
print ("Your question is",rand,operation,rand2)
d=int(input ("What is your answer:"))
if d==maths:
    print ("Correct, you may move to the next room")
else:
    print ("Incorrect. The actual answer is",maths)
