import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 16 * HEIGHT / 9
STARTING_POSITION = (0, -((HEIGHT/2)-20))

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= HEIGHT/2:
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_score()

screen.exitonclick()
