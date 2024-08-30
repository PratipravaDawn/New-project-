# import colorgram
# set =[]
# colours = colorgram.extract('Image.jpg', 6)
#
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     set.append(rgb)
#
# print(set)

colours = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 238), (145, 28, 66), (230, 237, 232)]

import random as r
import turtle
from turtle import Turtle, Screen

scrn = Screen()
carl = Turtle()
turtle.colormode(255)
carl.hideturtle()
carl.penup()
carl.speed("fastest")
carl.setheading(225)
carl.forward(300)
carl.setheading(360)

for dots in range(1,101):
    carl.dot(20, r.choice(colours))
    carl.forward(50)
    if dots % 10 == 0:
        carl.setheading(90)
        carl.forward(50)
        carl.setheading(180)
        carl.forward(500)
        carl.setheading(0)





scrn.screensize(10, 10)
scrn.exitonclick()