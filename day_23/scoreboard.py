from turtle import Turtle

FONT = ("Courier", 18, "normal")
HEIGHT = int(600)
WIDTH = int(16 * HEIGHT / 9)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(-((WIDTH/2) - 22), (HEIGHT/2) - 28)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
