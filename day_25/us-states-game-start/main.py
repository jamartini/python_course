from turtle import Turtle, Screen
from state_writer import State
import pandas

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the state", prompt="Type a state's name.")
answer_state = answer_state.title()
state_list = data.state.to_list()
correct_states = 0
guessed_states = []

game_is_on = True
while game_is_on:
    if answer_state == "Exit":
        break
    else:
        if answer_state in guessed_states:
            answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="Type a state's name.")
            answer_state = answer_state.title()
        elif answer_state in state_list:
            guessed_states.append(answer_state)
            correct_states += 1
            position = (int(data[data.state == f"{answer_state}"].x), int(data[data.state == f"{answer_state}"].y))
            new_correct_state = State(position, answer_state)
            answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="Type a state's name.")
            answer_state = answer_state.title()
        else:
            answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="Type a state's name.")
            answer_state = answer_state.title()
        if correct_states == 50:
            game_is_on = False

states_to_learn = {"states": [state for state in state_list if state not in guessed_states]}
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
