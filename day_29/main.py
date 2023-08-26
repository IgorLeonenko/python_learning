from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
  password_list = []
  p_letters = [random.choice(letters) for _ in range(2, 10)]
  p_numbers = [random.choice(numbers) for _ in range(2, 6)]
  p_symbols = [random.choice(symbols) for _ in range(2, 5)]

  password_list = p_letters + p_numbers + p_symbols
  random.shuffle(password_list)
  password = "".join(password_list)
  password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_record():
  site = website_input.get()
  login = login_input.get()
  password = password_input.get()
  item_dict = {
    "website": {
      "email": login,
      "password": password
    }
  }

  if len(site) == 0 or len(login) == 0 or len(password) == 0:
    messagebox.showinfo(title="Validation failed", message = "Fill all fields first!")
  else:
    is_ok = messagebox.askokcancel(title = "Save the data", message = f"You have to save:\n site: {site}\n login: {login}\n password: {password}")

    if is_ok:
      try:
        with open("data.json", "r") as file:
          data = json.load(file)
      except FileNotFoundError:
        with open("data.json", "w") as file:
          json.dump(item_dict, file, indent = 2)
      else:
        data.update(item_dict)
        with open("data.json", "w") as file:
          json.dump(data, file, indent = 2)
      finally:
        website_input.delete(0, END)
        password_input.delete(0, END)

#-----------------------------Search password---------------------------#
def search_data():
  website = website_input.get
  try:
    with open("data.json") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showinfo(title = "Error", message = "No data found")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title = website, message = f"Email: {email}\n password: {password}")
    else:
      messagebox.showinfo(title = "Error", message = "No website found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password manager')
window.config(padx = 50, pady = 40)

logo = PhotoImage(file = "logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 1, column = 1)

website_label = Label(text="Website").grid(row = 2, column = 0, sticky="e")
website_input = Entry(width = 35)
website_input.grid(row = 2, column = 1, columnspan = 2)
website_input.insert(END, 'site.com')
website_search_button = Button(text = "Search", command = search_data)
website_search_button.grid(row = 2, column = 2)

login_label = Label(text="Email/Username").grid(row = 3, column = 0, sticky="e")
login_input  = Entry(width = 35)
login_input.grid(row = 3, column = 1, columnspan = 2)
login_input.insert(END, 'example@email.com')

password_label = Label(text="Password").grid(row = 4, column = 0, sticky="e")
password_input = Entry(width = 21)
password_input.grid(row = 4, column = 1)
password_input.insert(END, "12345678")
password_generate_button = Button(text = "Generate", command = generate_password)
password_generate_button.grid(row = 4, column = 2)

add_button = Button(text = "Add", width = 36, comman=add_record).grid(row = 5, column = 1, columnspan = 2)

window.mainloop()