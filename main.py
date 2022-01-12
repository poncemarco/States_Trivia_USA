import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
# TODO Get the gif from the file and make it a turtle
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

'''
# TODO Get the x and y coords of the States in the turtle screen:
def get_mouse_click_coor(x, y):
    print(x, y)


# Seleccionamos del gif usando:
turtle.onscreenclick(get_mouse_click_coor)

'''

# The game begins!
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []
missing = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'Guess the State {len(guessed_states)}/{len(data.state)}', prompt="What's another state's name").capitalize()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
# TODO Save the missing states to a .csv
for state in all_states:
    if state in guessed_states:
        pass
    else:
        missing.append(state)

exit_data = pandas.DataFrame(missing)

exit_data.to_csv('You_missed_these.csv')








# Keep the screen open
turtle.mainloop()
