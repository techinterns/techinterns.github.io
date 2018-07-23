from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buddy.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return app.send_static_file('login.html')

@app.route('/register')
def register():
    return app.send_static_file('register.html')

@app.route('/forgot')
def reset_pass():
    return app.send_static_file('reset.html')