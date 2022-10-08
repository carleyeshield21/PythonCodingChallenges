from turtle import Turtle, Screen
Screen().bgcolor('lightgreen')
torus_turtle = Turtle()

torus_turtle.shape('turtle')
torus_turtle.speed('fastest')
torus_turtle.shapesize(2)
torus_turtle.stamp()

angle = 0
for n in range(180):
    print(n)
    angle += 2
    torus_turtle.left(angle)
    torus_turtle.penup()
    torus_turtle.forward(300)
    torus_turtle.pendown()
    for i in range(1):
        torus_turtle.color('brown')
        torus_turtle.right(-45)
        torus_turtle.circle(160, 90)
        torus_turtle.circle(160 / 2, 90)
        torus_turtle.circle(160, 90)
        torus_turtle.circle(160 / 2, 90)
    torus_turtle.penup()
    torus_turtle.home()

Screen().exitonclick()