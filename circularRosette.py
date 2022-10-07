import turtle
from turtle import Turtle, Screen
from random import *
screen = Screen()
screen.bgcolor('black')
turtle.colormode(255)

circ_turtle = Turtle()
circ_turtle.shape('turtle')
circ_turtle.speed('fastest')
circ_turtle.color('darkcyan')
for n in range(180):
    circ_turtle.color(randint(0,255),randint(0,255),randint(0,255))
    circ_turtle.circle(200)
    circ_turtle.left(2)
screen.exitonclick()