from turtle import Screen
from paddle import Paddle1, Paddle2
from scoreboard import Scoreboard1, Scoreboard2
from midline import MidLine
from ball import Ball
import time

HEIGHT = 600
WIDTH = int(16*HEIGHT/9)
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle_1 = Paddle1()
paddle_2 = Paddle2()
midline = MidLine()
score_1 = Scoreboard1()
score_2 = Scoreboard2()
ball = Ball()
ball.start_game()
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.0009)
    ball.move()
    screen.listen()
    screen.onkey(paddle_1.up, "w")
    screen.onkey(paddle_1.down, "s")
    screen.onkey(paddle_2.up, "Up")
    screen.onkey(paddle_2.down, "Down")
    for i in range(len(paddle_1.segments)):
        if paddle_1.segments[i].distance(ball) < 18:
            ball.bounce()
            ball.forward(10)
    for i in range(len(paddle_2.segments)):
        if paddle_2.segments[i].distance(ball) < 18:
            ball.bounce()
            ball.forward(10)
    if ball.ycor() > ((HEIGHT/2) - 11) or ball.ycor() < -((HEIGHT/2) - 11):
        ball.bounce_wall()
    if ball.xcor() > (WIDTH/2):
        ball.start_game()
        score_1.increase_score()
    if ball.xcor() < -(WIDTH/2):
        ball.start_game()
        score_2.increase_score()

screen.exitonclick()
