from flask import Flask, render_template, request, redirect, Response, jsonify
import random, json
import sys
from gmaps_calls import *

app = Flask(__name__)

@app.route("/")
def index():
    location = request.get_data()
    return render_template('index.html')

@app.route('/find', methods = ['POST','GET'])
def worker():
    data = request.get_data()

    return look_for([30.6131, -96.3218], data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
