from turtle import Turtle

HEIGHT = 600
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")


class Scoreboard1(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.setposition(-30, (HEIGHT/2)-30)
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', align="center", font=FONT)


class Scoreboard2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.setposition(30, (HEIGHT/2)-30)
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', align="center", font=FONT)
