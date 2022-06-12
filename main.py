import random
from unittest import result

print("Welcome to Rock, Paper, Scissors by Rejoice")
print("-------------------------------------------")

CPUscore = 0
Playerscore = 0
Tiescore = 0
PossibleHands = ["R","P","S"]

def CheckForWinner(Player, CPU):
    if(Player =="R" and CPU =="P"):
        print("You lose")
        return "CPU"
    elif(Player == "R" and CPU == "S"):
        print("You win")
        return "Player"
    elif(Player =="P" and CPU == "S"):
        print("You lose")
        return "CPU"
    elif(Player =="P" and CPU =="R"):
        print("You win")
        return "Player"
    elif(Player == "S" and CPU == "R"):
        print("You lose")
        return "CPU"
    elif(Player =="S" and CPU == "P"):
        print("You win")
        return "Player"
    else:
        print("It's a tie. Play again")  
        return "Tie"
       
while(Playerscore !=3 and CPUscore !=3):
    while True:
        Player = input("\nPick a hand. R, P, or S: ")
        if(Player == "R" or Player == "P" or Player == "S"):
            break
        else:
            print("Invalid input. Try again")

    CPU = random.choice(PossibleHands)

    print("Your hand: ", Player) 
    print("CPU hand: ", CPU)   
    result = CheckForWinner(Player, CPU)  
    if(result == "Player"):
        Playerscore += 1
    elif(result == "CPU"):  
        CPUscore += 1
    else:
        Tiescore += 0
    print("Your score: ", Playerscore, "CPU: ", CPUscore)

print("Game Over! Hope you enjoyed playing")
