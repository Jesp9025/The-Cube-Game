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
        
#Improved countdown timer        
def countdown(n):
  print("The game is gonna be", gameName)
  while n > 0:
    print(n, end="\r")
    n -= 1
    time.sleep(1)
  print("GO!")
