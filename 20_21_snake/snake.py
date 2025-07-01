from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEIGHT = 600
WIDTH = int(16*HEIGHT/9)


class Snake:
    def __init__(self):
        self.segments = []
        for xy in POSITIONS:
            self.add_segment(xy)
        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(WIDTH*2, HEIGHT*2)
        self.segments.clear()
        for xy in POSITIONS:
            self.add_segment(xy)
        self.head = self.segments[0]

    def move(self):
        for seg_i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_i - 1].xcor()
            new_y = self.segments[seg_i - 1].ycor()
            self.segments[seg_i].setposition(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
