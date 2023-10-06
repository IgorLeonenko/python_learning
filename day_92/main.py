from flask import Flask, render_template, redirect, request, url_for
import numpy as np
import io
from PIL import Image

app = Flask(__name__)
colors = []

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/palette")
def palette():
  global colors
  return render_template("palette.html", colors=colors)

@app.route("/process", methods=['POST'])
def process():
  global colors
  img = request.files['image']
  img_to_process = Image.open(io.BytesIO(img.read()))
  result = img_to_process.quantize(colors=10)
  palette = result.getpalette()
  colors = [tuple(palette[i:i+3]) for i in range(0, len(palette), 3) if tuple(palette[i:i+3]) != (0, 0, 0)]
  return redirect(url_for('palette'))


if __name__ == '__main__':
  app.run(debug=True)