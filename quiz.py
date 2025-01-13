#Ben Linhart
#1/9/2025
#Quiz

#int
import random
tq = 0     #int total questions
cq = 0     #int current questions
n1 = 0     #int number one
n2 = 0     #int number two
corr = 0   #int questions correct
#functions

def quiz():
    global tq, cq, n1, n2, corr
    print("Welcome to the multiplication quiz, answer to your best ability and wish you luck!")
    print(" ")
    print("Chose your difficulty: Easy, Medium, Hard")   # Tells computer level of difficulty
    diff = input("Chose your difficulty: Easy, Medium, Hard")
    if diff.lower() == "easy":                                       #Easy mode
        print(" ")
        print("How many total questions would you like to answer?")  # Tells the computer how many questions
        tq = int(input("How many total questions would you like to answer?"))
        for i in range(tq):
            n1 = random.randint(1,10)
            n2 = random.randint(1,10)
            ans = n1*n2
            cq = cq + 1
            print(" ")
            print("Question " + str(cq) + ": What is " + str(n1) + " X " + str(n2))
            ansp = int(input("Put your answer here"))
            if ans == ansp:
                print("You answered " + str(ansp) + " and you were correct!")
                corr = corr + 1
            else:
                print("You answered " + str(ansp) + " and you were wrong.")
    elif diff.lower() == "medium":                                           #Medium mode
        print(" ")
        print("How many total questions would you like to answer?")
        tq = int(input("How many total questions would you like to answer?"))
        for i in range(tq):
            n1 = random.randint(1,20)
            n2 = random.randint(1,20)
            ans = n1*n2
            cq = cq + 1
            print(" ")
            print("Question " + str(cq) + ": What is " + str(n1) + " X " + str(n2))
            ansp = int(input("Put your answer here"))
            if ans == ansp:
                print("You answered " + str(ansp) + " and you were correct!")
                corr = corr + 1
            else:
                print("You answered " + str(ansp) + " and you were wrong.")
    elif diff.lower() == "hard":                                             #Hard mode
        print(" ")
        print("How many total questions would you like to answer?")
        tq = int(input("How many total questions would you like to answer?"))
        for i in range(tq):
            n1 = random.randint(1,100)
            n2 = random.randint(1,100)
            ans = n1*n2
            cq = cq + 1
            print(" ")
            print("Question " + str(cq) + ": What is " + str(n1) + " X " + str(n2))
            ansp = int(input("Put your answer here"))
            if ans == ansp:
                print("You answered " + str(ansp) + " and you were correct!")
                corr = corr + 1
            else:
                print("You answered " + str(ansp) + " and you were wrong.")
    print(" ")
    print("You got " + str(corr) + " out of " + str(tq) + " Correct")


#Main
quiz()

