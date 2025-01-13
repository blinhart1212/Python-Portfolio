#Main
#Ben linhart 11/8 Number Guesser

#int
import random

def numberGuesser():
    print("Hello, you are playing the number guessing game.")
    dif = input("Chose your difficulty e=Easy m=Medium h=Hard")
    if dif == "e":
        print ("You're in Easy mode, give me a number 1-10")
        ans = random.randint(1,10)
        gue = int(input("Enter Number"))
        if ans == gue:
            print ("Hooray! You got it right")
        else:
            print ("you got it wrong the number was " + str(ans))
    elif dif == "m":
        print ("You're in Medium mode, give me a number 1-100")
        ans = random.randint(1,100)
        gue = int(input("Enter Number"))
        if ans == gue:
            print ("Hooray! You got it right")
        else:
            print ("you got it wrong the number was " + str(ans))
    elif dif == "h":
        print ("You're in Hard mode, give me a number 1-500")
        ans = random.randint(1,500)
        gue = int(input("Enter Number"))
        if ans == gue:
            print ("Hooray! You got it right")
        else:
            print ("you got it wrong the number was " + str(ans))
    pa = input ("Would you like to play again? (yes/no)")
    if pa == "yes":
        numberGuesser()
    else: print ("Have a great day!")

#main
numberGuesser()
