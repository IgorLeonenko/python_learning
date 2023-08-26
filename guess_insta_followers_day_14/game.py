from game_data import data
import random


init_answer = input("want to play higher/lower?: ")

def play_game():
  total_score = 0
  is_run = True
  take_rand_first = random.randint(0, len(data))
  take_rand_sec = random.randint(0, len(data))
  first = data[take_rand_first]
  second = data[take_rand_sec]

  while is_run:
    print(f"A: {first['name']} is a {first['description']} from {first['country']}")
    print(f"B: {second['name']} is a {second['description']} from {second['country']}")
    user_guess = input('Take a guess, who has more followers? a or b:')
    b = second['follower_count']
    a = first['follower_count']
    if user_guess == 'b':
      if b > a:
        total_score += 1
        print(f"Right! You guess it! Your total score: {total_score}")
      else:
        is_run = False
        print("Wrong! You lose!")
    elif user_guess == 'a':
      if a > b:
        total_score += 1
        print(f"Right! You guess it! Your total score: {total_score}")
      else:
        is_run = False
        print("Wrong! You lose!")


if init_answer == 'y':
  play_game()
