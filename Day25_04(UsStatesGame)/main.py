import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_data_frame = pandas.read_csv("50_states.csv")
game_on = True
states_guessed = []
all_states = state_data_frame["state"].to_list()
missing_states = []
while len(states_guessed) < 50:

    answer_state = screen.textinput(title=f"Guess the state - {len(states_guessed)}/50",
                                    prompt="What's another state name you wish to guess?").title()
    if answer_state == "Exit":
        # for state in all_states:
        #     if state not in states_guessed:
        #         missing_states.append(state)
        # Re-Doing the above using the  neat "List Comprehension"
        missing_states = [state for state in all_states if state not in states_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = state_data_frame[state_data_frame["state"] == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state)
        states_guessed.append(answer_state)




