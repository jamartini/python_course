from random import randint, choice
from turtle import Turtle

HEIGHT = 600
WIDTH = int(16*HEIGHT/9)
colors = ["orange", "blue", "yellow", "red", "green"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed(0)
        self.color(choice(colors))
        random_x = randint(int(-((WIDTH/2)-40)), int((WIDTH/2)-40))
        random_y = randint(int(-((HEIGHT/2)-40)), int((HEIGHT/2)-40))
        self.setposition(random_x, random_y)

    def refresh(self):
        self.color(choice(colors))
        random_x = randint(int(-((WIDTH/2)-40)), int((WIDTH/2)-40))
        random_y = randint(int(-((HEIGHT/2)-40)), int((HEIGHT/2)-40))
        self.setposition(random_x, random_y)
