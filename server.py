from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buddy.db'
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(120), unique=True, primary_key=True)

    def __repr__(self):
        return 'User {}'.format(self.email)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/login')
def login_page():
    return app.send_static_file('signup.html')