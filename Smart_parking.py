from flask import Flask, jsonify, request

import random

import threading

import time

app = Flask(_name_) parking_spots = [0] *10 # Represents 10 parking spots, initially all vacant

def simulate_iot_data():

global parking_spots

while True:

# Simulate IoT data (occupancy: 0 for vacant, 1 for occupied)

parking_spots = [random.randint(0, 1) for_in range(10)]

time.sleep(5) # Simulate data update every 5 seconds

@app.route('/parking', methods=['GET'])

def get_parking_status():

global parking_spots

return jsonify({'parking_status': parking_spots})
        if_name__ == '__main__':

# Start IoT data simulation in a separate thread

iot_thread = threading.Thread(target=simulate_iot_data)

iot_thread.daemon = True

iot_thread.start()

# Run the Flask app

app.run(debug=True)
