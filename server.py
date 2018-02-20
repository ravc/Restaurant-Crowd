from flask import Flask, render_template, request, redirect, Response, jsonify
import json, random, sys
from gmaps_calls import *

location = []

app = Flask(__name__)

@app.route('/')
def index():
    location = request.get_data()
    return render_template('index.html')

@app.route('/init', methods = ['POST', 'GET'])
def init():
    global location
    location = request.get_json()

    return look_for(location)

@app.route('/find', methods = ['POST', 'GET'])
def find():
    data = request.get_json()

    print(data)

    query = data[0]
    price = data[1]
    distance = data[2]

    return look_for(location, query=query, price=price, distance=distance)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
