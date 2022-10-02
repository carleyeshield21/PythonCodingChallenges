def polygon(n, num = int(input('How many sides do you want in the last polygon?\n'))):
    from turtle import Turtle, Screen
    import random

    poly_turtle = Turtle()
    poly_turtle.setpos(-45, 400)
    poly_turtle.shape('turtle')
    poly_turtle.speed('slow')
    poly_turtle.width(3)
    poly_turtle.color('blue')
    poly_turtle.penup()
    poly_turtle.forward(100)
    poly_turtle.pendown()

    s = n
    counter = 0
    while s<=n:
        rand_color = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        for i in range(n):
            poly_turtle.color(rand_color)
            poly_turtle.right(360/n)
            poly_turtle.forward(100)
        n +=1
        counter += 1
        print(counter)
        if counter == num - 2:
            break
    screen = Screen()
    screen.exitonclick()
polygon(3)