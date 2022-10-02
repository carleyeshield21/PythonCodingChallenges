# Another solution to polygon challenge
import  turtle as t
tart = t.Turtle()
def draw_shape(num_sides):
    import random
    rand_color = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    angle = 360 / num_sides
    for n in range(num_sides):
        tart.color(rand_color)
        tart.forward(100)
        tart.right(angle)
for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)