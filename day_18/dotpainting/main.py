import colorgram
from random import choice
from turtle import Turtle, Screen


timmy = Turtle()
timmy.pu()
timmy.hideturtle()
timmy.speed(0)
current_y = -225
timmy.goto(-225, current_y)
screen = Screen()
screen.colormode(255)

colors = colorgram.extract('image.jpg', 20)
color_palette = []

for i in range(len(colors)):
    new_color = (colors[i].rgb[0], colors[i].rgb[1], colors[i].rgb[2])
    color_palette.append(new_color)

for k in range(10):
    for j in range(10):
        timmy.dot(20, choice(color_palette))
        timmy.forward(50)
    current_y += 50
    timmy.goto(-225, current_y)

screen.exitonclick()
