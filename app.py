# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request, jsonify
import os
import math
import datetime


app = Flask(__name__)

@app.route('/')
def index():
    now_second = datetime.datetime.now().second
    sensor_values = math.sin(now_second)
    return render_template('index.html', value = sensor_values)

if __name__ == '__main__':
    app.run(debug=True)
