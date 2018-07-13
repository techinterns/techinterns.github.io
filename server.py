from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/resetpassword')
def reset_pass():
    return app.send_static_file('resetpassword.html')