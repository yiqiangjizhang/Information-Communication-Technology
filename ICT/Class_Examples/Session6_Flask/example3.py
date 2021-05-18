
# Import Flask
from flask import Flask
from sense_emu import SenseHat
import datetime
from flask import jsonify
from flask import request

sense = SenseHat()

# Store name of the program
app = Flask(__name__)

# Route of the app is the main route of the web server
@app.route('/')
# Function
def index():
    return "Raspberry PI ICT REST Server"


# Create a new temperature route
@app.route('/temperature')
# Function to get temperature from temperature sensor
def temp():
    temp = sense.get_temperature()
    # Create a dictionary
    data = dict()
    # Save variables
    data['temp'] = temp
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

@app.route('/temperature/pressure')
# Function to get temperature from pressure sensor
def temp_pressure():
    temp_p = sense.get_temperature_from_pressure()
    # Create a dictionary
    data = dict()
    # Save variables
    data['temp_p'] = temp_p
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

@app.route('/temperature/humidity')
# Function to get temperature from humidity sensor
def temp_humidity():
    temp_h = sense.get_temperature_from_humidity()
    # Create a dictionary
    data = dict()
    # Save variables
    data['temp_h'] = temp_h
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

# Pressure route
@app.route('/pressure')
# Function to get pressure from presure sensor
def pressure():
    pressure = sense.get_pressure()
    # Create a dictionary
    data = dict()
    # Save variables
    data['pressure'] = pressure
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

# Humidity route
@app.route('/humidity')
# Function to get pressure from presure sensor
def humidty():
    humidity = sense.get_humidity()
    # Create a dictionary
    data = dict()
    # Save variables
    data['humidity'] = humidity
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

# Compass route
@app.route('/compass')
# Function to get magnetometer (compass) from magnetometer sensor
def compass():
    compass = sense.get_compass()
    # Create a dictionary
    data = dict()
    # Save variables
    data['compass'] = compass
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)


# Accelerometer route
@app.route('/accelerometer')
# Function to get accelerometer from accelerometer sensor
def accelerometer():
    # Read accelerometer data from accelerometer sensor
    for i in range(0,10):
        accel_only = sense.get_accelerometer()
    pitch_acc = accel_only["pitch"]
    roll_acc = accel_only["roll"]
    yaw_acc = accel_only["yaw"]
    # Create a dictionary
    data = dict()
    # Save variables
    data['pitch_acc'] = pitch_acc
    data['roll_acc'] = roll_acc
    data['yaw_acc'] = yaw_acc
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

# Gyroscope route
@app.route('/gyroscope')
# Function to get gyroscope from gyroscope sensor
def gyroscope():
    # Read gyroscope data from gyroscope sensor
    for i in range(0,10):
        gyro_only = sense.get_gyroscope()
    pitch_gyro = gyro_only["pitch"]
    roll_gyro = gyro_only["roll"]
    yaw_gyro = gyro_only["yaw"]
    # Create a dictionary
    data = dict()
    # Save variables
    data['pitch_gyro'] = pitch_gyro
    data['roll_gyro'] = roll_gyro
    data['yaw_gyro'] = yaw_gyro
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)


# IMU route
@app.route('/imu')
# Function to get IMU from IMU sensor (processed)
def imu():
    # Read IMU data from IMU sensor (processed)
    for i in range(0,10):
        o = sense.get_orientation() # 'o' object is a dictionary
    pitch_IMU = o["pitch"]
    roll_IMU = o["roll"]
    yaw_IMU = o["yaw"]
    # Create a dictionary
    data = dict()
    # Save variables
    data['pitch_IMU'] = pitch_IMU
    data['roll_IMU'] = roll_IMU
    data['yaw_IMU'] = yaw_IMU
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)


## Requests
# http://127.0.0.1:5000/temperature/history?from=2021-05-11&to=2021-05-12

# Temperature history
@app.route('/temperature/history')
# Function to get IMU from IMU sensor (processed)
def temp_history():
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    print(from_date)
    print(to_date)
    temp = sense.get_temperature()
    return "Temperature: {0}".format(temp)

# Debug
if __name__ =='__main__':
    app.run(debug=True)








