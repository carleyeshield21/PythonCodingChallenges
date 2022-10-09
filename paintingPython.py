import turtle
import  random
from turtle import Turtle, Screen
turtle.colormode(255)

color_palette = [(220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47), (152, 207, 217), (8, 93, 113), (184, 185, 208), (74, 72, 37)]

paint_turtle = Turtle()
paint_turtle.shape('turtle')
paint_turtle.speed('fastest')
turtle.bgcolor('black')

y = -350
paint_turtle.penup()
paint_turtle.setpos(-350,y)
paint_turtle.pendown()

for i in range(20):
    for j in range(20):
        # =================================
        paint_turtle.fillcolor(random.choice(color_palette))
        paint_turtle.begin_fill()
        paint_turtle.circle(40)
        paint_turtle.end_fill()

        paint_turtle.fillcolor(random.choice(color_palette))
        paint_turtle.begin_fill()
        paint_turtle.circle(20)
        paint_turtle.end_fill()

        paint_turtle.left(90)
        paint_turtle.penup()
        paint_turtle.forward(40)
        paint_turtle.right(90)
        paint_turtle.pendown()

        paint_turtle.fillcolor(random.choice(color_palette))
        paint_turtle.begin_fill()
        paint_turtle.circle(20)
        paint_turtle.end_fill()

        paint_turtle.penup()
        paint_turtle.forward(80)
        paint_turtle.right(90)
        paint_turtle.forward(40)
        paint_turtle.left(90)
        # ================================
    y += 80
    paint_turtle.setpos(-350, y)

Screen().exitonclick()


# for i in range(len(color_palette)):
#     print(random.choices(color_palette))

# import colorgram
# colors = colorgram.extract('hirstimage.jpg', 50)
# mix_colors = []
# rgb_colors = []
# rgb_colors1 = []
# for color in colors:
#     mix_colors.append(color)
#     rgb_colors.append(color.rgb)
#
#     x = color.rgb.r
#     y = color.rgb.g
#     z = color.rgb.b
#
#     new_color = (x,y,z)
#
#     rgb_colors1.append(new_color)
#
# print(mix_colors)
# print('========')
# print(rgb_colors)
# print('========')
# print(rgb_colors1)