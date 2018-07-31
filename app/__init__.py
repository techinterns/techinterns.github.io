from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///..\\buddy.db'
app.config['SECRET_KEY'] = 'proof-of-concept' # This would be more secure if it wasn't a POC
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models