# Creating a polygon with n number of sides
def polygon(n=int(input('How many sides of polygon you want to draw?\n'))):
    from turtle import Turtle, Screen

    poly_turtle = Turtle()
    poly_turtle.setpos(-45, 400)
    poly_turtle.shape('turtle')
    poly_turtle.speed('slow')
    poly_turtle.width(3)
    poly_turtle.color('blue')
    poly_turtle.penup()
    poly_turtle.forward(100)
    poly_turtle.pendown()

    for i in range(n):
        poly_turtle.right(360 / n)
        poly_turtle.forward(100)
    n += 1
    screen = Screen()
    screen.exitonclick()
polygon()