from turtle import Turtle
FONT = ("Verdana", 8, "normal")


class State(Turtle):
    def __init__(self, position, state):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(position)
        self.write(f"{state}", align="center", font=FONT)
