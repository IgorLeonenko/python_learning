from turtle import Turtle

INIT_COORDS = [0, 20, 40]

class Snake():
  def __init__(self):
    self.segments = []

    for i in range(0, len(INIT_COORDS)):
      self.create_segment((-(INIT_COORDS[i]), 0))

    self.head = self.segments[0]

  def create_segment(self, position):
    segment = Turtle()
    segment.penup()
    segment.shape("square")
    segment.color("white")
    segment.goto(position)
    self.segments.append(segment)

  def move(self):
    start_position = len(self.segments) - 1
    for seg_num in range(start_position, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(20)

  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90)

  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)

  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0)

  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180)

  def add_segment(self):
    new_segment = self.segments[-1]
    self.create_segment(new_segment.position())

  def hit_border(self):
    x_coord = self.head.xcor()
    y_coord = self.head.ycor()
    return x_coord > 280 or x_coord < -280 or y_coord > 280 or y_coord < -280

  def reset(self):
    for el in self.segments:
      el.reset()
    self.segments.clear()
    for i in range(0, len(INIT_COORDS)):
      self.create_segment((-(INIT_COORDS[i]), 0))
    self.head = self.segments[0]