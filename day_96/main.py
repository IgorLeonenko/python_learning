import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

@app.route("/")
@app.route("/<int:page>")
def home(page=1):
  api_result = requests.get(f"{BASE_URL}?page={page}")
  breweries = api_result.json()

  meta_request = requests.get(f"{BASE_URL}/meta")
  meta_request = meta_request.json()
  pages_size = int(int(meta_request["total"]) / 50)

  return render_template("index.html", breweries=breweries, pages_size=pages_size)

@app.route("/page", methods=["GET", "POST"])
def paginate():
  page = request.form.get("page")
  return redirect(url_for('home', page=page))


if __name__ == '__main__':
  app.run(debug=True)