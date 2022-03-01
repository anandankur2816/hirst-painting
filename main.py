
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     col = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(col)
#
# print(rgb_colors)
import random
from turtle import Turtle,Screen

t=Turtle()
s=Screen()
s.colormode(255)
colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# t.dot(20,colors[4])

pos=t.pos()
# t.pendown()
t.speed(0)
t.up()
t.setheading(225)
t.forward(300)
t.setheading(0)
print(t.pos())
pos=t.pos()
t.hideturtle()

for _ in range(1,11):
    for i in range(10):
        t.dot(20,random.choice(colors))
        t.up()
        t.forward(30)
        t.down()
    t.up()
    t.setx(pos[0]+0)
    t.sety(pos[1]+_*30)
    # print(t.pos())

s.exitonclick()
