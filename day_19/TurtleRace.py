from turtle import Turtle, Screen
from random import randint

screen = Screen()
colors = ["red", "blue", "orange", "yellow", "purple", "green"]
y_positions = [-125, -75, -25, 25, 75, 125]
is_race_on = False
turtles = []

for i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.pu()
    new_turtle.color(colors[i])
    new_turtle.setposition(-230, y_positions[i])
    new_turtle.speed(10)
    turtles.append(new_turtle)


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(0, 6):
        turtles[i].forward(randint(0, 10))
        if turtles[i].xcor() > 230:
            is_race_on = False
            winner = turtles[i].pencolor()
            if user_bet.lower() == winner.lower():
                print(f"You won! The {winner} turtle is the winner.")
            else:
                print(f"You lost! The {winner} turtle is the winner.")


screen.exitonclick()
