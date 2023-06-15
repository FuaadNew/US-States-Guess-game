import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turt = turtle.Turtle()
game_on = True
turt.hideturtle()
turt.penup()
guessed_states = []
correctguess = 0
while len(guessed_states)<50:
    answer_state= screen.textinput(title= f"{correctguess}/50 States Correct", prompt = "What's another state name?" )
    data = pandas.read_csv("50_states.csv")
    if answer_state == "Exit":
        break
        #missing_states = [state for all_states if state not in guessed_states]
    for state in data["state"]:
        this_state =data[data.state==state]
        state_x = int(this_state.x)
        state_y = int(this_state.y)

        if state.lower() == answer_state.lower():
            correctguess+=1
            text = str(state)
            guessed_states.append(text)
            turt.setposition(state_x, state_y)
            turt.write(text, align="right")
            #state.goto(data[state]["x"]["y"])

Missedstates = {"MissedState":[]}
for state in data["state"]:
    if state not in guessed_states:
        Missedstates["MissedState"].append(state)


NewDataframe= pandas.DataFrame.from_dict(Missedstates)

NewDataframe.to_csv("MissedStates.csv")
