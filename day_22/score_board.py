from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self, position):
    super().__init__()
    self.total = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(position)
    self.show_score()

  def show_score(self):
    self.clear()
    self.write(f"{self.total}", align='center', font=('Arial', 24, 'normal'))

  def increase_score(self):
    self.total += 1
    self.show_score()