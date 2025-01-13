#Ben Linhart
#1/7
#rock paper scissors

#int
import random

#Functions

def rpsgame():
    ties = 0
    wins = 0
    losses = 0
    print ("Hello, you are playing Rock Paper Scissors, you know how to play what is your move?")
    while True:
        print (" ")
        print ("Win(s):" + str(wins) + " Loss(es):" + str(losses) + " Tie(s):" + str(ties))
        print (" ")
        ans = input("What is your move?")
        cans = random.randint(1,3)
        if ans.lower() == "rock":
            ans = 1
        elif ans.lower() == "paper":
            ans = 2
        elif ans.lower() == "scissors":
            ans = 3
        print ("The computer played:")
        if cans == 1:
            print("Rock")
        elif cans == 2:
            print("Paper")
        elif cans == 3:
            print("Scissors")
        if ans == cans:
            ties = ties + 1
            print ("You tied would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif ans == 1 and cans == 2:
            losses = losses + 1
            print("You lost, would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif ans == 1 and cans == 3:
            wins = wins + 1
            print("You won, would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif ans == 2 and cans == 1:
            wins = wins + 1
            print("You won, would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif ans == 2 and cans == 3:
            losses = losses + 1
            print("You lost, would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif ans == 3 and cans == 1:
            losses = losses + 1
            print("You lost, would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                break
        elif ans == 3 and cans == 2:
            wins = wins + 1
            print("You won, would you like to play again?")
            pa = input("yes/no")
            if pa == "no":
                print("Goodbye, have a good day")
                break

#main
rpsgame()

