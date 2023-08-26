from turtle import Turtle, Screen
import random
import colorgram

turtle = Turtle()
screen = Screen()
turtle.speed(0)
turtle.pensize(5)
screen.colormode(255)

colors = colorgram.extract('image.jpg', 10)

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

for i in range(50):
  color_choice = random.choice(colors).rgb
  r = color_choice.r
  g = color_choice.g
  b = color_choice.b
  turtle.color(r, g, b)
  turtle.dot()
  turtle.penup()
  turtle.forward(20)
  turtle.pendown()
  if i % 10 == 0:
    turtle.penup()
    turtle.goto(-300, i * 5)


# for i in range(4):
#   turtle.forward(100)
#   turtle.right(90)

# turtle.penup()
# turtle.goto(0, 100)

# for _ in range(10):
#   turtle.pendown()
#   turtle.forward(10)
#   turtle.penup()
#   turtle.forward(10)

# turtle.goto(0, 300)
# turtle.pendown()

# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     turtle.color(R, G, B)

# for i in range(3, 10):
#   change_color()
#   for _ in range(i):
#     turtle.forward(50)
#     turtle.right(360 / i)

# turtle.speed(0)

# def change_color():
#   R = random.random()
#   B = random.random()
#   G = random.random()
#   turtle.color(R, G, B)

# def draw_spirograph(gap_size):
#   for _ in range(int(360 / gap_size)):
#     change_color()
#     turtle.circle(100)
#     turtle.setheading(turtle.heading() + gap_size)

# draw_spirograph(10)
# turtle.pensize(3)
# directions = [0, 90, 180, 270]
# for _ in range(200):
#   change_color()
#   turtle.forward(30)
#   turtle.setheading(random.choice(directions))


screen.exitonclick()