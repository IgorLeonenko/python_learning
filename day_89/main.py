# from flask import Flask, render_template, redirect, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap

# app = Flask(__name__)

# ##Connect to Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# db = SQLAlchemy()
# db.init_app(app)

# ##Add bootstrap
# Bootstrap(app)

# ##TodoList configuration
# class TodoList(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(250), unique=True, nullable=False)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy()
db.init_app(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  completed = db.Column(db.Boolean, default=False)

with app.app_context():
  db.create_all()

@app.route('/')
def index():
  todos = Todo.query.all()
  return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
  content = request.form.get('content')
  if not content:
    return 'Content is required!', 400

  todo = Todo(content=content)
  db.session.add(todo)
  db.session.commit()

  return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle(id):
  todo = Todo.query.get(id)
  if not todo:
    return 'Todo not found!', 404

  todo.completed = not todo.completed
  db.session.commit()

  return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
  todo = Todo.query.get(id)
  if not todo:
    return 'Todo not found!', 404

  db.session.delete(todo)
  db.session.commit()

  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(debug=True)