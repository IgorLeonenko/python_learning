from flask import Flask
import random

random_nr = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:number>")
def guess_number(number):
  if number > random_nr:
    return "<h1 style='color:red'>Too high, try again!</h1>"
  elif number < random_nr:
    return "<h1 style='color:red'>Too low, try again!</h1>"
  else:
    return "<h1 style='color:green'>You found me!</h1>"


if __name__ == "__main__":
  app.run(debug=True)