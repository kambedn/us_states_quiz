import pandas
import turtle
IMAGE_PATH = "blank_states_img.gif"
PROMPT = "What's another state's name?"
DATA_PATH = "50_states.csv"
FONT = ('Arial', 8, 'bold')

# Creating the screen and changing its background to the US States image
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(800, 520)
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Reading csv data
data = pandas.read_csv(DATA_PATH)
# Extracting all states' names
states = data.state.to_list()

# Keeping track of the score
score = 0
max_score = len(states)

# Text turtle
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.speed(8)

# until the player guesses all the states
while score < max_score:

    # getting the guess
    answer_state = screen.textinput(title=f"{score}/{max_score} states correct", prompt=PROMPT).title()

    if answer_state == "Exit":  # secret option
        # If the player cannot guess all, the remaining states will be written into a csv file as a pandas series
        pandas.Series(states).to_csv("states_to_learn.csv")
        break

    if answer_state in states:  # if a guess is right
        score += 1  # increasing the score
        row = data[data.state == answer_state]  # extracting the row concerning the state
        x = row["x"].to_list()[0]  # extracting the x-coordinate
        y = row["y"].to_list()[0]  # extracting the y-coordinate
        text.goto(x, y)  # moving the text turtle to the state's location
        text.write(answer_state, align="center", font=FONT)  # writing the state's name on the map
        states.remove(answer_state)  # removing the state from the list with remaining states

print("Click on the screen to leave the program")
screen.exitonclick()
