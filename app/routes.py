from flask import redirect, url_for, render_template
from app import app, db
from app.models import User
from app.forms import LoginForm, RegisterForm

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/map')
    return render_template('login.html', form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/forgot')
def reset_pass():
    return app.send_static_file('reset.html')

@app.route('/map')
def map():
    return render_template('mapView.html', users=User.query.all())