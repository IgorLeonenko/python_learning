from turtle import Turtle, Screen
import random


screen = Screen()

# screen.listen()

# def move_forwards():
#   turtle.forward(10)

# def move_backs():
#   turtle.back(10)

# def move_clockwise():
#   heading = turtle.heading() + 10
#   turtle.setheading(heading)

# def move_counter_clockwise():
#   heading = turtle.heading() - 10
#   turtle.setheading(heading)

# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_backs, key="s")
# screen.onkey(fun=move_clockwise, key="a")
# screen.onkey(fun=move_counter_clockwise, key="d")
# screen.onkey(fun=turtle.reset, key="c")

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win? Choose color: ")

colors = ["purple", "orange", "green", "red", "black"]

turtle_list = []

for i in range(0, 5):
  turtle = Turtle(shape="turtle")
  turtle.color(colors[i])
  turtle.penup()
  if i > 3:
    y = (5 * i)
  else:
    y = -(20 * i)
  turtle.goto(-240, y)
  turtle_list.append(turtle)

if user_bet:
  race_is_run = True

while race_is_run:
  random_distance = random.randint(1, 10)
  moving_turtle = random.choice(turtle_list)
  moving_turtle.forward(random_distance)
  if moving_turtle.xcor() > 240:
    if moving_turtle.color() == user_bet:
      print("You win the bet!")
    else:
      print("You loose!")
    race_is_run = False
screen.bye()
