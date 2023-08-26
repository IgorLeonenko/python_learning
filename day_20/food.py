from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    self.move_position()

  def move_position(self):
    x_coord = random.randint(-280, 280)
    y_coord = random.randint(-280, 280)
    self.goto(x_coord, y_coord)