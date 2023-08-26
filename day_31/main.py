from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#-----------------------Read / Write data---------------------
card = {}
to_learn = {}

try:
  data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
  translation_frame = pandas.read_csv("./data/french_words.csv")
  to_learn = translation_frame.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records")


def next_card():
  global card, flip_timer
  window.after_cancel(flip_timer)
  card = random.choice(translation_frame)
  canvas_card.itemconfig(title, text = "French")
  canvas_card.itemconfig(word_text, text = card['French'])
  flip_timer = window.after(3000, func = flip_card)

def flip_card():
  canvas_card.itemconfig(title, text = "English")
  canvas_card.itemconfig(word_text, text = card['English'])

def save_progress():
  to_learn.remove(card)
  data = pandas.DataFrame(to_learn)
  data.to_csv("data/words_to_learn.csv", index=False)
  next_card()

# ----------------UI------------------
window = Tk()
window.title('Flashy')
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

card_image = PhotoImage(file = "./images/card_front.png")
canvas_card = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas_card.create_image(400, 263, image = card_image)
title = canvas_card.create_text(400, 150, text = "", font = ("Ariel", 40, "italic", "bold"), fill="black")
word_text = canvas_card.create_text(400, 263, text = '', font = ("Ariel", 60), fill="black")
canvas_card.grid(row = 0, column = 0, columnspan = 2)


cross_image = PhotoImage(file = "./images/wrong.png")
wrong_button = Button(text = "wrong", image = cross_image, highlightthickness = 0, command = next_card)
wrong_button.grid(row = 1, column = 0, sticky = "w")

check_image = PhotoImage(file = "./images/right.png")
right_button = Button(text = "right", image = check_image, highlightthickness = 0, command = save_progress)
right_button.grid(row = 1, column = 1, sticky = "e")

next_card()

window.mainloop()
