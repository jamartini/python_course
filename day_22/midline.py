from turtle import Turtle

HEIGHT = 600


class MidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.setposition(0, -(HEIGHT/2))
        self.setheading(90)
        while self.ycor() < (HEIGHT/2):
            self.pd()
            self.forward(15)
            self.pu()
            self.forward(15)
