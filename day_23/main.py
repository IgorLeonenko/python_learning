from turtle import Screen
from player import Player
from cars import Cars
from score import Score
import time
import random

screen = Screen()

screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
screen.onkey(player.up, "Up")

cars = Cars()
score = Score()

game_is_on = True

while game_is_on:
  time.sleep(0.5)
  screen.update()
  cars.create_car()
  cars.move()

  for car in cars.all_cars:
    if player.distance(car) < 15:
      score.game_over()
      game_is_on = False

  if player.cross_top():
    player.base_position()
    score.increase_score()

screen.exitonclick()