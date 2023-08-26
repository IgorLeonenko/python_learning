from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text = "00:00")
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
  global reps
  reps += 1
  work_secs = WORK_MIN * 60
  short_break_secs = SHORT_BREAK_MIN * 60
  long_break_secs = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    count_down(long_break_secs)
    timer_label.config(text = "Break")
  elif reps % 2 == 0:
    count_down(short_break_secs)
    timer_label.config(text = "Break")
  else:
    count_down(work_secs)
    timer_label.config(text = "Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
  global timer
  count_mins = math.floor(count / 60)
  count_secs = count % 60
  if count_secs < 10:
    count_secs = f"0{count_secs}"
  canvas.itemconfig(timer_text, text = f"{count_mins}:{count_secs}")
  if count > 0:
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomidorro')
window.geometry('345x300')
timer_label = Label(text="Timer", font=(FONT_NAME, 20), fg = GREEN).grid(row = 0, column = 1)

photo = PhotoImage(file = "tomato.png")
canvas = Canvas(width = 200, height = 224)
canvas.create_image(103, 112, image = photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

button_start = Button(text = "Start", command = start_timer).grid(row = 3, column = 0)
checkmark = Label(text="✓", font=(FONT_NAME, 30), fg = GREEN).grid(row = 3, column = 1)
button_reset = Button(text = "Reset", command = reset_timer).grid(row = 3, column = 2)


window.mainloop()