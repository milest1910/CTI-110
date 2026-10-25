
# Troy Miles Jr
# 10/20/2026
# P4LAB1
# This program uses turtle graphics to draw a house using a square and a triangle with for and while loops.
# Hey user, guess what? THis program may or may not run. Just get used to it at this point.

# Import turtle library
import turtle

# Create screen and set background color
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle object
house = turtle.Turtle()
house.color("darkgreen")
house.pensize(3)
house.speed(3)

# Move turtle to starting position
house.penup()
house.goto(-75, -100)
house.pendown()

# Draw square using for loop
for side in range(4):
    house.forward(150)
    house.left(90)

# Move turtle to top of square
house.penup()
house.goto(-75, 50)
house.setheading(0)
house.pendown()

# Draw triangle roof using while loop
house.fillcolor("green")
house.begin_fill()

count = 0

while count < 3:
    house.forward(150)
    house.left(120)
    count = count + 1

house.end_fill()

# Hide turtle after drawing
house.hideturtle()

# Keep screen open
turtle.done()
