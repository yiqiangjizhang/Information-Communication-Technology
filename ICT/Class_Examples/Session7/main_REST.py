
# Import Flask
from flask import Flask, redirect
from sense_emu import SenseHat
import datetime
from flask import jsonify
from flask import request
import sqlite3
import sys

sense = SenseHat()

# Store name of the program
app = Flask(__name__)

# Route of the app is the main route of the web server
@app.route('/')
# Function
def index():
    message = "Raspberry PI ICT REST Server"
    return message

# Function to check if database is used by a process
def is_open(conn):
     try:
        conn.cursor()
        return True
     except Exception as ex:
        print(ex)
        return False

# Open database
sqlite_file = "database.db"

# Connection
conn = sqlite3.connect(sqlite_file)


# Create a new sensors route
# (http://127.0.0.1:5000/sensors?origin={temperature,pressure,humidity,accelerometer,gyroscope,magnetometer,imu})
@app.route('/sensors')
# Function to show all available sensors
def sensors():
    origin = request.args.get('origin')
    if origin is None:
        # Create a dictionary
        data = dict()
        # Save variables
        data['00_message'] = "Sensors:"
        data['temperature'] = "Temperature"
        data['pressure'] = "Pressure"
        data['humidity'] = "Humidity"
        data['accelerometer'] = "Accelerometer"
        data['gyroscope'] = "Gyroscope"
        data['magnetometer'] = "Magnetometer"
        data['imu'] = "IMU"
        return jsonify(data)

    else:
        if origin == 'temperature':
            return redirect('/sensors/temperature')
        elif origin == 'pressure':
            return redirect('/sensors/temperature')
        elif origin == 'humidity':
            return redirect('/sensors/humidity')
        elif origin == 'acceloremeter':
            return redirect('sensors/accelerometer')
        elif origin == 'gyroscope':
            return redirect('sensors/gyroscope')
        elif origin == 'magnetometer':
            return redirect('sensors/magnetometer')
        elif origin == 'imu':
            return redirect('sensors/imu')


## Sensors
# Create a new temperature route 
@app.route('/sensors/temperature')
# Function to get temperature from temperature sensor
def temp(): 
    temp = sense.get_temperature()
    # Create a dictionary
    data = dict()
    # Save variables
    data['temp'] = temp
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

@app.route('/sensors/temperature/pressure')
# Function to get temperature from pressure sensor
def temp_pressure():
    temp_p = sense.get_temperature_from_pressure()
    # Create a dictionary
    data = dict()
    # Save variables
    data['temp_p'] = temp_p
    data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
    return jsonify(data)

@app.route('/sensors/temperature/humidity')
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
@app.route('/sensors/pressure')
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
@app.route('/sensors/humidity')
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
@app.route('/sensors/compass')
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
@app.route('/sensors/accelerometer')
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
@app.route('/sensors/imu')
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


## History Requests
# http://127.0.0.1:5000/sensors/temperature/history?from=2021-05-11&to=2021-05-12

# Temperature history
@app.route('/sensors/temperature/history')
# Request history 
def temp_history():
    conn = sqlite3.connect(sqlite_file)
    from_date = request.args.get('from')
    to_date = request.args.get('to')

    from_date_complete = from_date + "T00:00:00"
    to_date_complete = to_date + "T23:59:59"

    # TODO: Check datetime converti dtring to date time

    # query = "SELECT sensors.name, variables.name, measures.measure, max(measures.date), variables.units FROM sensors, variables, measures WHERE sensors.id = variables.sensor_id AND variables.id = measures.variable_id GROUP BY variables.id"

    query = "SELECT * FROM measures WHERE date > '{0:}' AND date < '{1:}' AND variable_id = 5".format(from_date_complete , to_date_complete)

    if True:
    # if is_open(conn):
        # Cursor for commands and accessing information
        rows = None
        try:
            print("A",file=sys.stderr)
            cur = conn.cursor()
            print("B",file=sys.stderr)

            cur.execute(query)
            rows = cur.fetchall()
            print("Measures in database",file=sys.stderr)
            print(rows,file=sys.stderr)
        except Exception as e:
            print(e, file=sys.stderr)

    else:
        print("Database is currently being used")
        # WRITE ERROR MSG

    return jsonify(rows)


# Debug
if __name__ =='__main__':
    app.run(debug=True)



