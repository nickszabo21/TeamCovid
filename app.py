import pandas as pd
import os
import json
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    result = render_template("index.html")
    return result

@app.route("/first")
def first():
    result = render_template("first.html")
    return result

@app.route("/national")
def national():
    result = render_template("national.html")
    return result

@app.route("/city")
def city():
    result = render_template("city.html")
    return result



if __name__ == "__main__":
    app.run(debug=True)
