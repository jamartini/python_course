from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

HEIGHT = 600
WIDTH = int(16*HEIGHT/9)

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def press_space():
    return True


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() > (WIDTH/2)-10 or snake.head.xcor() < -((WIDTH/2)-10) or snake.head.ycor() > (HEIGHT/2)-10 or \
            snake.head.ycor() < -((HEIGHT/2)-10):
        snake.reset()
        scoreboard.reset_score()
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset_score()

scoreboard.reset_score()

screen.exitonclick()
