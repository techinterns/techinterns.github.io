from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///..\\buddy.db'
db = SQLAlchemy(app)

from app import routes, models