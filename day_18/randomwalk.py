from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
screen.colormode(255)
timmy.pd()
timmy.pensize(10)
timmy.speed(0)

for i in range(20):
    choices = ['forward', 'backward', 'right', 'left']
    next_move = choice(choices)
    if next_move == 'forward':
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.forward(50)
    elif next_move == 'backward':
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.right(180)
        timmy.forward(50)
    elif next_move == 'right':
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.right(90)
        timmy.forward(50)
    else:
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.left(90)
        timmy.forward(50)

screen.exitonclick()
