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

@app.route("/")
def page_two():
    result = render_template("page_two.html")
    return result

@app.route("/")
def page_three():
    result = render_template("page_three.html")
    return result


if __name__ == "__main__":
    app.run(debug=True)
