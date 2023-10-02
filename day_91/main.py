## for speech-to-text used https://large-text-to-speech.p.rapidapi.com

import tkinter as tk
from tkinter import filedialog, Label, Button
import PyPDF2
import requests
import json
import os

apikey = os.environ['STT_APIKEY']
filename = "speech.wav"

headers = {
  'content-type': "application/json",
  'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com",
  'x-rapidapi-key': apikey
}

window = tk.Tk()
window.title("Add watermarks")
window.minsize(width=500, height=150)
window.config(bg="grey")


def process_pdf():
    global text
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
      pdf_file = open(file_path, 'rb')
      pdfreader = PyPDF2.PdfReader(pdf_file)
      text = ""
      for page_num in range(0, len(pdfreader.pages)):
          page_text = pdfreader.pages[page_num].extract_text()
          text += page_text.replace('\n', ' ')
      pdf_file.close()

      start_processing_text()

def start_processing_text():
  label.config(text="Starting text processing...")
  window.after(100, send_request_to_api)

def send_request_to_api():
  response = requests.request("POST", "https://large-text-to-speech.p.rapidapi.com/tts", data=json.dumps({"text": text}), headers=headers)
  id = json.loads(response.text)['id']
  eta = json.loads(response.text)['eta']
  label.config(text=f"Waiting {eta} seconds for the job to finish...")
  window.after(eta * 1000, fetch_result, id)

def fetch_result(id):
  response = requests.request("GET", "https://large-text-to-speech.p.rapidapi.com/tts", headers=headers, params={'id': id})

  if "url" in json.loads(response.text):
    handle_download(json.loads(response.text)['url'])
  else:
    label.config(text="Waiting...")
    window.after(3000, fetch_result, id)

def handle_download(url):
    response = requests.request("GET", url)
    with open(filename, 'wb') as f:
      f.write(response.content)
    label.config(text=f"File saved to {filename} !")

label = Label(window, font=("Curier", 20), fg="white", bg="grey")
label.place(x=80, y=120)

button = Button(text="Upload pdf", highlightthickness=0, command=process_pdf)
button.place(x=200, y=80)

window.mainloop()
