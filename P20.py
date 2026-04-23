#Tyler Nguyen

import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Draw face (green circle)
t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.circle(150)

# Left eye (red)
t.penup()
t.goto(-60, 80)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(25)
t.end_fill()

# Right eye (blue)
t.penup()
t.goto(60, 80)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(25)
t.end_fill()

# Nose (yellow rectangle)
t.penup()
t.goto(-40, 20)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(2):
    t.forward(80)
    t.right(90)
    t.forward(15)
    t.right(90)
t.end_fill()

# Mouth (black triangle)
t.penup()
t.goto(-50, -40)
t.pendown()
t.color("black")
t.pensize(5)
t.begin_fill()
t.goto(50, -40)
t.goto(0, -110)
t.goto(-50, -40)
t.end_fill()

# Hide turtle
t.hideturtle()

turtle.done()
