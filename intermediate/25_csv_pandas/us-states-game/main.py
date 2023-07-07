import turtle
from typing import List

import pandas as pd
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()
score = scoreboard.score

states = pd.read_csv("50_states.csv")
states_dict = pd.DataFrame.to_dict(states)
guessed_states = []
missing_state = []
for state in states_dict["state"]:
    missing_state.append(states_dict["state"][state])

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    for state in range(50):
        if answer_state == states_dict["state"][state]:
            guessed_states.append(answer_state)
            missing_state.remove(answer_state)
            position = state
            scoreboard.write_state(x=states_dict["x"][position],y=states_dict["y"][position],state_name=states_dict["state"][state])
            score += 1




df = pd.DataFrame(missing_state)
df.to_csv("states_to_learn.csv")
