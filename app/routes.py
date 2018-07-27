from flask import redirect, url_for, render_template
from app import app, db
from app.models import User

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

@app.route('/map')
def map():
    return render_template('mapView.html', users=User.query.all())