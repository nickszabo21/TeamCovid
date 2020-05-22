import pandas as pd
import os
import json
from flask import Flask, jsonify, render_template


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    result = render_template("index.html")
    return result

@app.route("/global")
def global():
    result = render_template("global.html")
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
