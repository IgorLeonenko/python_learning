import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

read_data = pandas.read_csv("50_states.csv")
states = read_data.state.to_list()
guessed_states = []

def coord(direction, state):
  row = read_data[read_data.state == state]
  if direction == "x":
    return row.x.item()
  elif direction == "y":
    return row.y.item()

def pin_state(user_answer):
  x = coord("x", user_answer)
  y = coord("y", user_answer)
  guessed_state = turtle.Turtle()
  guessed_state.hideturtle()
  guessed_state.penup()
  guessed_state.goto(x, y)
  guessed_state.write(f"{user_answer}", align='center', font=('Arial', 12, 'normal'))


while len(guessed_states) < 50:
  user_answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="What another state name? \n Type exit to quit").capitalize()
  if user_answer == "Exit":
    missing_states = [state for state in states if state not in guessed_states]
    data_dict = { "state": missing_states }
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("missed_states.csv")
    break

  if user_answer in states:
    guessed_states.append(user_answer)
    pin_state(user_answer)

turtle.mainloop()