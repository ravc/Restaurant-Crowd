from flask import Flask, render_template, request, redirect, Response, jsonify
import random, json
import sys
from gmaps_calls import *

latlon = []

app = Flask(__name__)

@app.route("/")
def index():
    location = request.get_data()
    return render_template('index.html')

@app.route('/find', methods = ['POST','GET'])
def find():
    look = str(request.get_data())

    x = look.split('&')

    query = x[0][4:]
    price = int(x[1][2])
    distance = int(x[2][2:-1])
    
    return look_for(latlon, query=query, price=price, distance=distance)

@app.route('/init', methods = ['POST', 'GET'])
def init():
    data = str(request.get_data())
    
    x = data.split('&')
    
    latitude = float(x[-3].split('=')[1])
    longitude = float(x[-2].split('=')[1])
    
    global latlon
    latlon = [latitude,longitude]

    return look_for(latlon)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
