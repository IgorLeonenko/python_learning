import tkinter as tk
from tkinter import Text

class TextWipeoutApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Text Wipeout App")
    self.label = tk.Label(self, text="Type below. If you stop for 5 seconds, text will disappear:")
    self.label.pack(pady=10)
    self.text_area = Text(self, height=100, width=150)
    self.text_area.pack(padx=10, pady=10)
    self.text_area.bind('<KeyRelease>', self.reset_timer)
    self.after_id = None

  def reset_timer(self):
    if self.after_id:
      self.after_cancel(self.after_id)

    self.after_id = self.after(5000, self.clear_text)

  def clear_text(self):
    self.text_area.delete(1.0, tk.END)
    self.after_id = None

if __name__ == "__main__":
  app = TextWipeoutApp()
  app.mainloop()
