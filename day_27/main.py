from tkinter import *


window = Tk()
window.title("Miles to km converter")
window.minsize(width = 300, height = 150)


input = Entry(width = 10)
input.place(x = 80, y = 20)

Label(text="miles").place(x = 190, y = 20)
label_output = Label(text=f"is equal to 0 km", font=("Lucida Console", 20))
label_output.place(x = 70, y = 50)

def calculate():
  mi = float(input.get())
  km = round(mi * 1.68)
  label_output["text"] = f"is equal to {km} km"

button = Button(text = "calculate", command = calculate)
button.place(x = 80, y = 80)

window.mainloop()