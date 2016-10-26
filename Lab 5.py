#Lab 5

from turtle import *
bob = Turtle()

screen = bob.getscreen()

rent = screen.numinput("How much for rent?","How much will you spend on rent?")
utilities = screen.numinput("How much for utilities?","How much will you spend on utilities?")
food = screen.numinput("How much for food?","How much will you spend on food?")
fun = screen.numinput("How much for fun?","How much will you spend on fun?")

def setup():
    bob.setheading(0)
    bob.pendown
    bob.color("black","blue")
    bob.begin_fill()
    
#first find the largest to make it red


def findlargest():
    global rent, utlities, food, fun
    if rent > utilities:
        if rent > food:
            if rent > fun:
                return rent
    if utilities > rent:
        if utilities > food:
            if utilities > fun:
                return utilities
    if food > rent:
        if food > utilities:
            if food > fun:
                return food
    if fun > rent :
        if fun > utilities:
            if fun > food:
                return fun
def title():
    bob.penup()
    bob.goto(-75,300)
    bob.write("Monthly Expenses",font = ('Arial',12,'bold'))

x = -100
y = 0
width = 50
space = 25

def labels(x,y,label):
    x = x - width
    y = y - 17
    bob.goto(x,y)
    bob.write(label)
    
def dollar(x,y,label):
    x = x - width
    y = label/2.5   
    bob.goto(x,y)
    bob.write('$'+str(int(label))) #im converting it to int first to get rid of decimal

#draw bars
def draw_bar(x,y,height,width):
    global bob 
    bob.goto(x,y)
    setup() 
    for i in range(2):
        bob.left(90)
        bob.forward(height/2.5) 
        bob.left(90)
        bob.forward(width)
    bob.end_fill()
    bob.penup()

#draw red
def draw_red(x,y,height,width):
    global bob 
    bob.goto(x,y)
    bob.setheading(0)
    bob.pendown
    bob.color("black","red")
    bob.begin_fill() 
    for i in range(2):
        bob.left(90)
        bob.forward(height/2.5) 
        bob.left(90)
        bob.forward(width)
    bob.end_fill()
    bob.penup()

title()
largest = findlargest()


height = rent
draw_bar(x,y,height,width)
labels(x,y,'Rent')
dollar(x,y,rent)
if largest == rent:
    draw_red(x,y,height,width)

x = x + width + space


height = utilities
draw_bar(x,y,height,width)
labels(x,y,'Utilities')
dollar(x,y,utilities)
if largest == utilities:
    draw_red(x,y,height,width)
x = x + width + space

height = food
draw_bar(x,y,height,width)
labels(x,y,'Food')
dollar(x,y,food)
if largest == food:
    draw_red(x,y,height,width)
x = x + width + space

height = fun
draw_bar(x,y,height,width)
labels(x,y,'Fun')
dollar(x,y,fun)
if largest == fun:
    draw_red(x,y,height,width)



#im overlapping the previously drawn graph w a red one 

