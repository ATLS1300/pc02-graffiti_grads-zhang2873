#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Amy Zhang
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======


turtle.penup()
turtle.goto(120,-120)

turtle.fillcolor("purple")
turtle.begin_fill()
turtle.pendown()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()

turtle.pensize(4)
turtle.penup()
turtle.goto(150,150)


turtle.pendown()
turtle.circle(50)


turtle.pensize(2)
turtle.penup()
turtle.goto(-100,100)

turtle.pencolor("pink")
turtle.fillcolor(255,192,203)
turtle.begin_fill()

turtle.pendown()
turtle.backward(50)
turtle.left(60)
turtle.backward(50)
turtle.left(60)
turtle.backward(50)
turtle.left(60)
turtle.backward(50)
turtle.left(60)
turtle.backward(50)
turtle.left(60)
turtle.backward(50)
turtle.end_fill()

turtle.pencolor(13,152,186)
turtle.pensize(5)
turtle.penup()
turtle.goto(-120,-120)

turtle.shape("arrow")
turtle.pendown()
turtle.forward(100)

turtle.penup()
turtle.shape("circle")

turtle.goto(20,105)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(20)

turtle.end_fill()
turtle.pen(up)


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
