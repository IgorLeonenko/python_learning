from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
screen.listen()
# screen.tracer(0)

pad_1 = Paddle(position=(370, 0))
screen.onkey(pad_1.up, "Up")
screen.onkey(pad_1.down, "Down")
score_1 = ScoreBoard((200, 260))

pad_2 = Paddle(position=(-370, 0))
screen.onkey(pad_2.up, "w")
screen.onkey(pad_2.down, "s")
score_2 = ScoreBoard((-200, 260))

ball = Ball()

game_is_on = True

while game_is_on:
  time.sleep(0.05)
  screen.update()
  ball.move()
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  if ball.distance(pad_1) < 50 and ball.xcor() > 350 or ball.distance(pad_2) < 50 and ball.xcor() < -350:
    ball.bounce_x()

  if ball.xcor() > 400:
    ball.reset_position()
    score_2.increase_score()

  if ball.xcor() < -400:
    ball.reset_position()
    score_1.increase_score()




screen.exitonclick()