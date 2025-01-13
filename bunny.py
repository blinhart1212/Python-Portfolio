#Heading

#Init
import turtle
wenjian = turtle.Turtle()
wenjian.speed(10)
ben = turtle.Turtle()
ben.speed(10)

#Function
#Craft the circular head of the bunny wenjian
def head():
    wenjian.circle(150, 360)
#Craft the first ear of the bunny wenjian
def ear1():
    wenjian.penup()
    wenjian.goto(-75, 280)
    wenjian.left(90)
    wenjian.pendown()
    wenjian.forward(75)
    wenjian.circle(-30, 180)
    wenjian.forward(58)
#Craft the other ear wenjian
def ear2():
    wenjian.penup()
    wenjian.goto(75,280)
    wenjian.left(180)
    wenjian.pendown()
    wenjian.forward(75)
    wenjian.circle(30, 180)
    wenjian.forward(58)
#Makes the eye wenjian
def eye():
    for i in range(1):
        wenjian.dot(40, "black")
        wenjian.dot(10, "white")
#Makes eyebrow wenjian
def eyebrow():
    for i in range(1):
        wenjian.circle(20, 180)
#Makes nose wenjian
def nose():
    for i in range(3):
        wenjian.left(90)
        wenjian.left(45)
        wenjian.forward(20)

#Make Mouth wenjian
def mouth():
    wenjian.pensize(5)
    wenjian.goto(5,100)
    wenjian.right(50)
    wenjian.forward(10)
    wenjian.circle(-10, 180)
    wenjian.penup()
    wenjian.goto(5,100)
    wenjian.pendown()
    wenjian.left(180)
    wenjian.forward(8)
    wenjian.circle(10,180)

#Make Whiskers wenjian
def whisker():
    wenjian.pendown()
    wenjian.backward(10)
    wenjian.penup()

#Makes InnerEar Ben
def innerEar1():
    ben.penup()
    ben.goto(-60,288)
    ben.pendown()
    ben.left(180)
    ben.forward(50)
    ben.circle(-15,180)
    ben.forward(43)

#Makes another inner ear Ben
def innerEar2():
    ben.penup()
    ben.goto(60,288)
    ben.pendown()
    ben.right(180)
    ben.forward(50)
    ben.circle(15,180)
    ben.forward(43)

#Makes the bunny's body Ben
def body():
    ben.penup()
    ben.goto(-70,15)
    ben.pendown()
    ben.forward(125)
    ben.circle(37,180)
    ben.right(180)
    ben.circle(37,180)
    ben.forward(125)

#Makes the bunny's first leg Ben
def leg1():
    ben.penup()
    ben.goto(-70,-35)
    ben.pendown()
    ben.left(140)
    ben.circle(200,20)
    ben.right(90)
    ben.circle(50,20)
    ben.circle(20,180)
    ben.forward(50)

#Makes the bunny's other leg Ben
def leg2():
    ben.penup()
    ben.goto(79,-30)
    ben.pendown()
    ben.right(51)
    ben.circle(-200,20)
    ben.left(90)
    ben.circle(-50,20)
    ben.circle(-20,180)
    ben.forward(50)

#Makes the bunny's tail Ben
def tail():
    ben.penup()
    ben.goto(90,-45)
    ben.pendown()
    ben.right(45)
    for i in range(3):
        ben.circle(-15,180)
        ben.left(90)

#Makes the bunny's beard Ben
def beard():
    ben.pensize(7)
    ben.penup()
    ben.goto(-32.5,5)
    ben.pendown()
    ben.circle(28,120)
    ben.left(120)
    ben.circle(-15,70)
    ben.right(150)
    ben.circle(30,100)
    ben.left(35)
    ben.circle(30,100)
    ben.right(150)
    ben.circle(-15,70)
    ben.left(120)
    ben.circle(28,120)

def bunny():
    wenjian.pensize(10)
    head()
    ear1()
    ear2()
    wenjian.penup()
    wenjian.goto(75, 120)
    eye()
    wenjian.goto(-75, 120)
    eye()
    wenjian.left(180)
    wenjian.goto(90, 220)
    wenjian.pendown()
    eyebrow()
    wenjian.left(180)
    wenjian.penup()
    wenjian.goto(-60, 220)
    wenjian.pendown()
    eyebrow()
    wenjian.penup()
    wenjian.goto(0, 100)
    wenjian.pendown()
    nose()
    mouth()
    wenjian.penup()
    wenjian.goto(70, 80)
    whisker()
    wenjian.goto(80, 80)
    whisker()
    wenjian.goto(90, 80)
    whisker()
    wenjian.goto(-70, 80)
    whisker()
    wenjian.goto(-80, 80)
    whisker()
    wenjian.goto(-90, 80)
    whisker()
    wenjian.hideturtle()
    ben.right(90)
    ben.pensize(5)
    innerEar1()
    innerEar2()
    ben.pensize(10)
    body()
    leg1()
    leg2()
    tail()
    beard()
    ben.hideturtle()

#Main
bunny()



