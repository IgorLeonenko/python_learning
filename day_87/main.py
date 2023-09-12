from turtle import Screen
from turtle import Turtle
import time

class Paddle(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("blue")
    self.setheading(90)
    self.shapesize(stretch_len=1, stretch_wid=10)
    self.goto(0, -170)

  def left(self):
    self.goto(self.xcor() - 40, self.ycor())

  def right(self):
    self.goto(self.xcor() + 40, self.ycor())

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("white")
    self.x_cor = 10
    self.y_cor = 10

  def move(self):
    new_x = self.xcor() + self.x_cor
    new_y = self.ycor() + self.y_cor
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.y_cor *= -1

  def bounce_x(self):
    self.x_cor *= -1

  def reset_position(self):
    self.goto(0, 0)
    self.bounce_x()

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.total = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(400, 170)
    self.show_score()

  def show_score(self):
    self.clear()
    self.write(f"{self.total}", align='center', font=('Arial', 24, 'normal'))

  def increise_score(self):
    self.total += 1
    self.show_score()

class Block(Turtle):
  def __init__(self, color):
    super().__init__()
    self.color(color)

  def create_block(self, pos_x, pos_y):
    self.penup()
    self.goto(pos_x, pos_y)
    self.shape("square")
    self.setheading(180)
    self.shapesize(stretch_len=5, stretch_wid=1)


  def gap(self):
    self.forward(20)


screen = Screen()
screen.setup(width=1000, height=400)
screen.bgcolor('black')
screen.title("Breakout")
screen.tracer(0)
screen.listen()

pad = Paddle()
screen.onkey(pad.left, "Left")
screen.onkey(pad.right, "Right")

ball = Ball()

score = ScoreBoard()

block_colors = ['red', 'blue', 'green']
all_blocks = []

for color in block_colors:
  for n in range(0, 9):
    block = Block(color)
    block.create_block(-445 + n * 110, 140 - block_colors.index(color) * 30)
    all_blocks.append(block)


game_is_on = True

while game_is_on:
  end_game = Turtle()
  end_game.color("white")
  end_game.hideturtle()
  time.sleep(0.05)
  screen.update()
  ball.move()

  if ball.ycor() > 180:
    ball.bounce_y()
  if ball.ycor() < -180:
    end_game.write("GAME OVER, YOU LOOSE", align='center', font=('Arial', 44, 'normal'))
    game_is_on = False
  if ball.xcor() > 480 or ball.xcor() < -480:
    ball.bounce_x()
  if ball.distance(pad) < 70 and ball.ycor() < -140:
    ball.bounce_y()
  if len(all_blocks) == 0:
    end_game.write("GAME OVER, YOU WIN", align='center', font=('Arial', 44, 'normal'))
    game_is_on = False
  for block in all_blocks:
    if ball.distance(block) < 50:
      block.ht()
      block.clear()
      all_blocks.remove(block)
      ball.bounce_y()
      score.increise_score()

screen.exitonclick()