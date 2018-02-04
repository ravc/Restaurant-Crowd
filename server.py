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
    data = request.get_data()
    
    return look_for(latlon, data)

@app.route('/init', methods = ['POST', 'GET'])
def init():
    data = str(request.get_data())
    
    x = data.split('&')
    
    latitude = float(x[-3].split('=')[1])
    longitude = float(x[-2].split('=')[1])
    
    global latlon
    latlon = [latitude,longitude]
    
    return look_for([latitude,longitude])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
