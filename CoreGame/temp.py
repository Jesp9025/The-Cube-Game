#Function to choose difficulty
def difficulty():
    global pointsToWin
    while True:
        choice = input("Please choose a difficulty..\na: Easy\nb: Veteran\nc: Global Elite\nYour choice: ").upper()
        if choice == "A":
            pointsToWin = 5
            break
        elif choice == "B":
            pointsToWin = 10  
            break
        elif choice == "C":
            pointsToWin = 15
            break


            
#https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#Function to clear the terminal         
def clearTerminal():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else: #Linux and Mac
        print("\033c", end="")
        
def countdown(n=3):
  print("The game is gonna be", gameName)
  time.sleep(1)
  while n > 0:
    print(n, end="\r") # end="\r" removed the previously printed text
    n -= 1
    time.sleep(1)
  print("GO!")

#Asks if player is ready to start or not
def ready():
    while True:
        choice = input("Well then, are you ready to play the game? (type 'yes' or 'no'): ").upper()
        if choice == "YES" or choice == "Y":
            break
        elif choice == "NO" or choice == "N":
            sys.exit(print("Well goodbye then"))   
        else:
            print ("We just told you to enter 'Yes' or 'No' for crying out loud.")
