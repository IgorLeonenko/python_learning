from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("white")
    self.setheading(90)
    self.shapesize(stretch_len=5, stretch_wid=1)
    self.goto(position)


  def up(self):
    self.forward(30)

  def down(self):
    self.back(30)
