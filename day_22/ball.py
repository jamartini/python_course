from turtle import Turtle
from random import randint

HEIGHT = 600
WIDTH = int(16*HEIGHT/9)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.should_move = False
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.pu()
        self.speed(0)

    def start_game(self):
        self.setposition(0, 0)
        self.setheading(randint(170, 190))

    # def start_moving(self):
    #     self.should_move = True
    #     self.move()

    def move(self):
        self.forward(6)

    def bounce(self):
        previous_heading = self.heading()
        if previous_heading > 90 or previous_heading < 270:
            if previous_heading > 180:
                self.setheading(360 - (previous_heading - 180) + randint(-5, 5))
            elif previous_heading < 180:
                self.setheading(180 - previous_heading + randint(-5, 5))
            elif previous_heading == 180 and self.ycor() > 0:
                self.setheading(randint(355, 360))
            elif previous_heading == 180 and self.ycor() < 0:
                self.setheading(randint(0, 5))
        elif previous_heading < 90 or previous_heading > 270:
            if previous_heading > 180:
                self.setheading(previous_heading + 90 + randint(-5, 5))
            if previous_heading < 180:
                self.setheading(previous_heading - 90 + randint(-5, 5))
            if (previous_heading == 0 or previous_heading == 360) and self.ycor() < 0:
                self.setheading(randint(174, 179))
            elif (previous_heading == 0 or previous_heading == 360) and self.ycor() > 0:
                self.setheading(randint(181, 185))

    def bounce_wall(self):
        previous_heading = self.heading()
        if 0 < previous_heading < 180:
            if previous_heading > 90:
                self.setheading(180 + (180 - previous_heading) + randint(-5, 5))
            elif previous_heading < 90:
                self.setheading(270 + (90 - previous_heading) + randint(-5, 5))
        elif 180 < previous_heading < 360:
            if previous_heading > 270:
                self.setheading(360 - previous_heading + randint(-5, 5))
            if previous_heading < 270:
                self.setheading(90 + (270 - previous_heading) + randint(-5, 5))
