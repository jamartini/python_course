from turtle import Turtle, Screen
from random import randint


timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
screen.colormode(255)
timmy.pd()
timmy.pensize(1)
timmy.speed(0)

for i in range(60):
    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.circle(100)
    timmy.left(6)

screen.exitonclick()
