import pandas as pd
import os
import json
from flask import Flask, jsonify


app = Flask(__name__)
app.config[""] = (


@app.route("/")
def index():
    result = render_template("index.html")
    return result