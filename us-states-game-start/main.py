import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

FONT = ('Arial', 10, 'normal')

correct_guesses = []
df = pandas.read_csv('50_states.csv')

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Correct Guesses",
                                    prompt="What's another state's name?")

    if len(correct_guesses) != 50:
        if answer_state.title() == 'Exit':
            missing_states = [state for state in df['state'] if state not in correct_guesses]
            new_data = pandas.DataFrame(missing_states)
            print(new_data)
            #new_data.to_csv('States_to_Learn.csv')
            break

        for state in df['state']:
            if answer_state.lower() == state.lower() and state not in correct_guesses:
                # Correct State
                correct_guesses.append(state)
    else:
        # All answers right
        game_is_on = False

    # Place state names on map
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    x_corr = df[df['state'] == correct_guesses[-1]]['x'].values[0]
    y_corr = df[df['state'] == correct_guesses[-1]]['y'].values[0]
    label.goto(x_corr, y_corr)
    label.write(correct_guesses[-1], align='center', font=FONT)
