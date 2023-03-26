from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
screen.colormode(255)

for i in range(4, 11):
    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for k in range(i):
        timmy.right(360/i)
        timmy.forward(100)

screen.exitonclick()
