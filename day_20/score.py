from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.total_score = 0
    self.high_score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 280)
    self.show_score()

  def reset(self):
    if self.total_score > self.high_score:
      self.high_score = self.total_score
      with open("high_score.txt", mode="w") as file:
        file.write(str(self.high_score))
    self.total_score = 0
    self.show_score()

  def show_score(self):
    self.clear()
    with open("high_score.txt") as file:
      high_score = file.read()
    self.write(f"Score: {self.total_score}  |  High score: {high_score} ", align='center', font=('Arial', 14, 'normal'))

  def increase_score(self):
    self.total_score += 1
    self.show_score()

  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write("Game over", align='center', font=('Arial', 20, 'normal'))