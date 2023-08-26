from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.total = 0
    self.color("black")
    self.hideturtle()
    self.penup()
    self.goto(-250, 280)
    self.show_score()

  def show_score(self):
    self.clear()
    self.write(f"Level: {self.total}", align='center', font=('Arial', 14, 'normal'))

  def game_over(self):
    self.goto(0, 0)
    self.write(f"Game over", align='center', font=('Arial', 14, 'normal'))

  def increase_score(self):
    self.total += 1
    self.show_score()