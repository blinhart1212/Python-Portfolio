#ben linhart
#10/18
# Cat name generator


print("Welcome to the cat name generator!")
print("Answer the questions to see what ur cat name would be!")
while True:
    ans = input("Boy cat (b) or girl cat (g)?")
    if ans == "b":
        ans = input("No hair (no) or with hair (yes)?")
        if ans == "no":
            ans = input("Black(b) or White(w)?")
            if ans == "b":
                print ("Your cat name will be Charcoal!")
            else:
                print ("Your cat name will be Cloud!")
        else:
            ans = input("Cream(c) or Tabby(t)")
            if ans == "c":
                print ("Your cat name will be Milkshake!")
            else:
                print ("Your cat name will be Maple!")
    else:
        ans = input("Stripes(s) or Dots(d)")
        if ans == "s":
            ans = input("Grey(g) or Orange(o)")
            if ans == "g":
                print ("Your cat name will be Chrome!")
            else:
                print ("Your cat name will be Tiger!")
        else:
            ans = input ("Brown(b) or Tricolor(t)")
            if ans == "b":
                print ("Your cat name will be Sugar!")
            else:
                print ("Your cat name will be Stormy!")
    ans = input ("Would you like to play again (yes) or (no)?")
    if ans == "no":
        print ("Thank you for doing the cat name simulator")
        break




