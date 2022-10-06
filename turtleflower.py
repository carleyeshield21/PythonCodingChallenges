import turtle
from turtle import Turtle, Screen
from random import*

turtle_flower = Turtle()
turtle_flower.shape('turtle')
turtle_flower.shapesize(2)
turtle_flower.width(10)
turtle_flower.speed('fastest')
turtle.colormode(255)
Screen().bgcolor('blue')

for repetition in range(100):
    x = randint(-250,250)
    y = randint(-250,250)

    for i in range(4):
        turtle_flower.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle_flower.right(90)
        turtle_flower.circle(50, 90)
        # turtle_flower.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle_flower.circle(50 / 2, 90)
        # turtle_flower.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle_flower.circle(50, 90)
        # turtle_flower.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle_flower.circle(50 / 2, 90)
    turtle_flower.penup()
    turtle_flower.setpos(x,y)
    turtle_flower.pendown()

Screen().exitonclick()