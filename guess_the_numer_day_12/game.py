#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choosed_numer = random.randrange(1, 100)
print(f"Pssst, the correct answer is {choosed_numer}")

is_wrong_level = True

while is_wrong_level:
  level_choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level_choose == "hard" or level_choose == "easy":
    is_wrong_level = False

attempts = 0

if level_choose == "hard":
  attempts = 5
elif level_choose == "easy":
  attempts = 10

gamer_lose = False

while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  gamer_choice = int(input("Make a guess: "))
  if gamer_choice < choosed_numer:
    print("Too low")
    attempts -= 1
    if attempts == 0:
      gamer_lose = True
  elif gamer_choice > choosed_numer:
    print("Too high")
    attempts -= 1
    if attempts == 0:
      gamer_lose = True
  elif gamer_choice == choosed_numer:
    print("You guessed numberd. You win!")
    attempts = 0

if gamer_lose:
  print("Your attempts finished. You loose!")