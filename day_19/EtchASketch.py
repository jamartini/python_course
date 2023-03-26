from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_right():
    timmy.right(15)


def turn_left():
    timmy.left(15)


def clear_screen():
    timmy.clear()
    timmy.pu()
    timmy.home()
    timmy.pd()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
