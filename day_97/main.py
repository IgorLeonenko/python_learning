from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onlineshop.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

stripe.api_key = 'sk_test_51O7LLPEl4RGDpLV3bjUfa0BDrH7MrjZOLVo2Vgm5sZDzybDk4ycCQuuEdL3CDo09ekOwaKYD2CzDRM9k78mrkRVB007k2wLcK8'

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  is_active = db.Column(db.Boolean, default=True)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  price = db.Column(db.Float, nullable=False)
  image = db.Column(db.String(220), nullable=True)

class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
  quantity = db.Column(db.Integer, nullable=False)

def prefill_db():
  product1 = Product(name="Jacket", image="https://cdn-images.farfetch-contents.com/21/35/94/65/21359465_51374776_600.jpg", price=119.99)
  product2 = Product(name="Sweater", image="https://media.lexception.com/img/products/olow/96969-olow-pullrandom-01-0800-0800.jpg", price=29.99)
  product3 = Product(name="Boots", image="https://img.ltwebstatic.com/images3_pi/2023/09/25/2f/1695631017fd7406576f5f7fbbbcb231e5b27a8288_thumbnail_720x.webp", price=40.99)

  db.session.add(product1)
  db.session.add(product2)
  db.session.add(product3)
  db.session.commit()

with app.app_context():
  db.create_all()
  products = Product.query.all()
  if len(products) == 0:
    prefill_db()

@app.route('/register_page', methods=['GET'])
def register_page():
  return render_template('register_page.html')

@app.route('/login_page', methods=['GET'])
def login_page():
  return render_template('login_page.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  email = request.form.get('email', '')
  username = request.form.get('username', '')
  password = request.form.get('user_password', '')
  hashed_password = ''

  if username == '' and User.query.filter_by(username=username).first():
    flash('Username already exists or empty.', 'error')
    return redirect(url_for('register_page'))

  if email == '' and User.query.filter_by(email=email).first():
    flash('Email already exists or empty.', 'error')
    return redirect(url_for('register_page'))

  if len(password) < 8:
    flash('Password must be at least 8 characters long.', 'error')
    return redirect(url_for('register_page'))
  else:
    hashed_password = generate_password_hash(password, method='sha256')

  new_user = User(username=username, email=email, password=hashed_password)
  db.session.add(new_user)
  db.session.commit()

  flash('Your account has been created!', 'success')
  return redirect(url_for('login_page'))

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
      login_user(user)
      return redirect(url_for('index'))
    else:
      flash('Login unsuccessful. Check username and password.')
  return render_template('login_page.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route('/')
def index():
  products = Product.query.all()
  return render_template('index.html', products=products)

@app.route('/add_to_cart/<product_id>')
@login_required
def add_to_cart(product_id):
  if 'cart' not in session:
    session['cart'] = []

  session['cart'].append(product_id)
  session.modified = True
  return redirect('/')

@app.route('/remove_from_cart/<product_id>')
@login_required
def remove_from_cart(product_id):
  session['cart'].remove(product_id)
  session.modified = True
  return redirect('/cart_page')

@app.route('/cart_page', methods=['GET'])
@login_required
def cart_page():
  cart_items = []
  total = 0
  if len(session['cart']) > 0:
    cart_items = Product.query.filter(Product.id.in_(session['cart'])).all()
    total = sum(item.price for item in cart_items)
  return render_template('cart_page.html', cart_items=cart_items, total=total)

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
  total = request.form.get('total')

  intent = stripe.PaymentIntent.create(
    amount=int(float(total) * 100),
    currency='usd'
  )

  items = Product.query.filter(Product.id.in_(session['cart'])).all()
  for item in items:
    new_order = Order(user_id=current_user.id, product_id=item.id, quantity=1)
    db.session.add(new_order)
    db.session.commit()

  session['cart'] = []

  flash('Thank you for you order!', 'success')
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)