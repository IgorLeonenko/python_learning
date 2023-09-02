import tkinter
from tkinter import *
import random
import time

texts = [
  "The quick brown fox jumps over the lazy dog.",
  "In a small town not far from the city, a young artist named Emily was working on her latest masterpiece.",
  "Programming languages like Python, Java, and C++ have become essential tools in the modern world."
]

text = random.choice(texts)

window = Tk()
window.title("Typing speed test")
window.minsize(width=500, height=400)

all_text = Text(window, width=60, height=10)
all_text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
all_text.insert(tkinter.END, text)
typed_text = Text(window, width=60,height=10)
typed_text.place(relx=0.5, rely=0.7,anchor=tkinter.CENTER)

start_time = None

def start():
  global start_time
  start_time = time.time()
  window.after(100, count_text)

def count_text():
  global start_time
  all_text_get = all_text.get("1.0",'end-1c')
  typed_text_get = typed_text.get("1.0",'end-1c')
  if all_text_get == typed_text_get:
    end_time = time.time()
    elapsed_time = end_time - start_time
    words = len(typed_text_get.split())
    per_minute = (words / elapsed_time) * 60
    label.config(text=f"Done! Your typing speed is {per_minute:.2f} words per minute")
  else:
    window.after(100, count_text)

label = Label(window, font=("Curier", 20), fg = "white")
label.place(x = 10, y = 45)

button = Button(text = "Start test", highlightthickness = 0, command = start)
button.place(x = 220, y = 15)

window.mainloop()