from turtle import Screen
from turtle import Turtle
import random
import time

ALIEN_COLORS = ["red", "blue", "green", "white"]

class Alien(Turtle):
  def __init__(self, x_coord, y_coord, color):
    super().__init__()
    self.penup()
    self.shape("triangle")
    self.color(color)
    self.setheading(270)
    self.goto(x_coord, y_coord)

  def change_y_position(self):
    self.goto(self.xcor(), self.ycor() - 0.05)

  def drop_bomb(self):
    return AlienBomb(self.xcor(), self.ycor())


class AlienBomb(Turtle):
  def __init__(self, x_coord, y_coord):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_len=0.5, stretch_wid=1)
    self.goto(x_coord, y_coord)

  def move(self):
    self.goto(self.xcor(), self.ycor() - 10)

class Defender(Turtle):
  def __init__(self):
    super().__init__()
    self.lasers = []
    self.penup()
    self.shape("square")
    self.color("blue")
    self.setheading(90)
    self.shapesize(stretch_len=1, stretch_wid=2)
    self.goto(0, -300)

  def left(self):
    self.goto(self.xcor() - 10, self.ycor())

  def right(self):
    self.goto(self.xcor() + 10, self.ycor())

  def laser_beam(self):
    laser_beam = Laser(self.xcor())
    self.lasers.append(laser_beam)

class Laser(Turtle):
  def __init__(self, x_coord):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("yellow")
    self.shapesize(stretch_len=0.5, stretch_wid=1)
    self.goto(x_coord, -295)

  def move(self):
    self.goto(self.xcor(), self.ycor() + 10)

def end_game():
  end_game = Turtle()
  end_game.color("red")
  end_game.hideturtle()
  end_game.write("GAME OVER, YOU LOOSE", align='center', font=('Arial', 44, 'normal'))

screen = Screen()
screen.setup(width=1100, height=700)
screen.bgcolor('black')
screen.title("Alien invaders")
screen.tracer(0)
screen.listen()

defender = Defender()
screen.onkey(defender.left, "Left")
screen.onkey(defender.right, "Right")
screen.onkey(defender.laser_beam, "space")

aliens = []
total_bombs = []
lasers = defender.lasers
game_is_on = True

for i in range(1, 5):
  color = random.choice(ALIEN_COLORS)
  ALIEN_COLORS.remove(color)
  for n in range(-10, 12):
    aliens.append(Alien(n * 50, (80 * i), color))

while game_is_on:
  time.sleep(0.05)
  screen.update()

  for laser in lasers:
    laser.move()
    if laser.ycor() > 370:
      lasers.remove(laser)
      laser.clear()

  for alien in aliens:
    alien.change_y_position()

    if defender.distance(alien) < 5 and alien.ycor() < -298:
      end_game()
      game_is_on = False

    for laser in lasers:
      if laser.distance(alien) < 5:
        lasers.remove(laser)
        aliens.remove(alien)
        laser.ht()
        alien.ht()
        laser.clear()
        alien.clear()


  if len(total_bombs) > 0:
    [bomb.move() for bomb in total_bombs]

  if len(total_bombs) < 3:
    bomb_dropper = random.choice(aliens)
    bomb = bomb_dropper.drop_bomb()
    total_bombs.append(bomb)

  for bomb in total_bombs:
    if bomb.ycor() < -350:
      total_bombs.remove(bomb)
      bomb.clear()
    if defender.distance(bomb) < 5 and bomb.ycor() < -298:
      end_game()
      game_is_on = False
    for laser in lasers:
      if laser.distance(bomb) < 10:
        total_bombs.remove(bomb)
        lasers.remove(laser)
        bomb.ht()
        laser.ht()
        bomb.clear()
        laser.clear()

screen.exitonclick()