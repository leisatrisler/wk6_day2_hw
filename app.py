import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hello/leisa")
def hello_there():
    return render_template('leisa.html')
