from turtle import Turtle

HEIGHT = 600
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")
GAME_OVER_FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.pu()
        self.setposition(0, (HEIGHT/2)-30)
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align="center", font=("Verdana", 10, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score} High Score: {self.high_score}', align="center", font=("Verdana", 10, "normal"))
