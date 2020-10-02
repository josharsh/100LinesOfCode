import turtle

import colorsys

import random

turtle.bgcolor("black")

turtle.speed(0)

x=random.randint(1, 999999999)

y=random.randint(1, 999999999)

for i in range(1001):

    color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)

    turtle.color(color)

    turtle.forward(i)

    turtle.right(x)

    turtle.left(y)
    
turtle.done()