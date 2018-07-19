from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buddy.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/resetpassword')
def reset_pass():
    return app.send_static_file('resetpassword.html')