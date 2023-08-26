from turtle import Turtle
import random

COLORS = ["orange", "red", "green", "purple", "black", "yellow"]

class Cars():
  def __init__(self):
    self.all_cars = []

  def create_car(self):
    car = Turtle()
    car.color(random.choice(COLORS))
    car.penup()
    car.shape("square")
    car.setheading(180)
    car.shapesize(stretch_len=2, stretch_wid=1)
    rand_y = random.randint(-260, 260)
    car.goto(265, rand_y)
    self.all_cars.append(car)

  def move(self):
    for car in self.all_cars:
      car.forward(20)
