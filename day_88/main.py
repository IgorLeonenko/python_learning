from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

##Add bootstrap
Bootstrap(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(250), unique=True, nullable=False)
  map_url = db.Column(db.String(500), nullable=False)
  img_url = db.Column(db.String(500), nullable=False)
  location = db.Column(db.String(250), nullable=False)
  seats = db.Column(db.String(250), nullable=False)
  has_toilet = db.Column(db.Boolean, nullable=False)
  has_wifi = db.Column(db.Boolean, nullable=False)
  has_sockets = db.Column(db.Boolean, nullable=False)
  can_take_calls = db.Column(db.Boolean, nullable=False)
  coffee_price = db.Column(db.String(250), nullable=True)

@app.template_filter('bool_to_yes_no')
def bool_to_yes_no(value):
  return "Yes" if value == True else "No"

app.add_template_filter(bool_to_yes_no, name='bool_to_yes_no')

@app.route("/")
def home():
  result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
  all_cafes = result.scalars().all()
  return render_template("index.html", cafes=all_cafes)

@app.route("/new", methods=["GET"])
def new_cafe():
  return render_template("new.html")

@app.route("/add", methods=["GET", "POST"])
def add_new_cafe():
  new_cafe = Cafe(
    name=request.form.get("name"),
    map_url=request.form.get("map_url"),
    img_url=request.form.get("img_url"),
    location=request.form.get("location"),
    has_sockets=bool(request.form.get("sockets")),
    has_toilet=bool(request.form.get("toilet")),
    has_wifi=bool(request.form.get("wifi")),
    can_take_calls=bool(request.form.get("calls")),
    seats=request.form.get("seats"),
    coffee_price=request.form.get("coffee_price"),
  )
  db.session.add(new_cafe)
  db.session.commit()
  return redirect("/", code=302)

@app.route("/delete_cafe/<int:cafe_id>", methods=["GET", "DELETE"])
def delete_cafe(cafe_id):
  cafe = db.get_or_404(Cafe, cafe_id)
  if cafe:
    db.session.delete(cafe)
    db.session.commit()
    return redirect("/", code=302)

if __name__ == '__main__':
  app.run(debug=False)
