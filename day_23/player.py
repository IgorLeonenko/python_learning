from turtle import Turtle

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("turtle")
    self.setheading(90)
    self.base_position()

  def up(self):
    self.forward(20)

  def base_position(self):
    self.goto(0, -280)

  def cross_top(self):
    return self.ycor() > 290