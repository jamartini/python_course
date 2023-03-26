from turtle import Turtle

HEIGHT = 600
WIDTH = int(16*HEIGHT/9)
POSITIONS_1 = [(-((WIDTH/2)-30), 20), (-((WIDTH/2)-30), 0), (-((WIDTH/2)-30), -20)]
POSITIONS_2 = [((WIDTH/2)-30, 20), ((WIDTH/2)-30, 0), ((WIDTH/2)-30, -20)]
MOVE_DISTANCE = 20


class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        for xy in POSITIONS_1:
            self.add_segment(xy)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def up(self):
        self.head = self.segments[0]
        self.head.setheading(90)
        for seg_i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_i - 1].xcor()
            new_y = self.segments[seg_i - 1].ycor()
            self.segments[seg_i].setposition(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def down(self):
        self.head = self.segments[2]
        self.head.setheading(270)
        for seg_i in range(0, len(self.segments) - 1):
            new_x = self.segments[seg_i + 1].xcor()
            new_y = self.segments[seg_i + 1].ycor()
            self.segments[seg_i].setposition(new_x, new_y)
        self.segments[2].forward(MOVE_DISTANCE)


class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        for xy in POSITIONS_2:
            self.add_segment(xy)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def up(self):
        self.head = self.segments[0]
        self.head.setheading(90)
        for seg_i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_i - 1].xcor()
            new_y = self.segments[seg_i - 1].ycor()
            self.segments[seg_i].setposition(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def down(self):
        self.head = self.segments[2]
        self.head.setheading(270)
        for seg_i in range(0, len(self.segments) - 1):
            new_x = self.segments[seg_i + 1].xcor()
            new_y = self.segments[seg_i + 1].ycor()
            self.segments[seg_i].setposition(new_x, new_y)
        self.segments[2].forward(MOVE_DISTANCE)
