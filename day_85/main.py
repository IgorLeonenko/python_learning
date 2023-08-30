import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Add watermarks")
window.minsize(width = 400, height = 150)
window.config(bg = "grey")
image_path = ""

def upload_photo():
  global image_path
  image_path = select_image_dialog()

def upload_watermark():
  if image_path != "":
    logo_path = select_image_dialog()
    logo_image = Image.open(logo_path).convert("RGBA")
    image = Image.open(image_path).convert("RGBA")

    logo_width, logo_height = logo_image.size
    image_width, image_height = image.size

    if logo_width > image_width or logo_height > image_height:
      logo_image.thumbnail((image_width / 2, image_height / 2))

    logo_x, logo_y = 0
    image.paste(logo_image, (logo_x, logo_y), mask=logo_image)
    image.show()
  else:
    messagebox.showinfo(title = "Error", message = "No image uploaded")

def select_image_dialog():
  return filedialog.askopenfilename(title="Select an Image", filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg')))


button = tk.Button(text = "Upload photo", highlightthickness = 0, command = upload_photo)
button.place(x = 50, y = 80)

button = tk.Button(text = "Upload watermark", highlightthickness = 0, command = upload_watermark)
button.place(x = 200, y = 80)

window.mainloop()