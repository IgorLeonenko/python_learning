from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
snake = Snake()
food = Food()
score = Score()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True


while game_is_on:
  score
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) < 15:
    food.move_position()
    score.increase_score()
    snake.add_segment()

  if snake.hit_border():
    score.reset()
    snake.reset()

  for segment in snake.segments[1::]:
    if snake.head.distance(segment) < 10:
      score.reset()
      snake.reset()

screen.exitonclick()