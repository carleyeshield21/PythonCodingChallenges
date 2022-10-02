import random
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(0,0,'pink')

koopa_king = Turtle()
koopa_king.shape('turtle')
koopa_king.shapesize(2)
koopa_king.width(15)
koopa_king.color('darkcyan')
koopa_king.speed('fastest')

arr = []
for x in range(361):
    arr.append(x)

for i in range(10000):
    rand_color = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    koopa_king.right(random.choice(arr))
    koopa_king.color(rand_color)
    koopa_king.circle(30,300)

# screen.screensize()
# screen.exitonclick()
# rand_color = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
# screen.screensize()
# (400, 300)
# screen.screensize(2000,1500)
# screen.screensize()
# (2000, 1500)