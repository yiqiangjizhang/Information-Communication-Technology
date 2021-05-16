
# Import Flask
from flask import Flask
from sense_emu import SenseHat
import datetime
from flask import jsonify

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
    response = list()
    for _ in range(0,10):
        data = dict()
        data['temp'] = temp
        data['time_stamp'] = "{0:%Y-%m-%dT%H:%M:%S.%fZ}".format(datetime.datetime.utcnow())
        data['additional'] = dict()
        data['additional']['a'] = 3
        data['additional']['b'] = 56
        response.append(data)
    return jsonify(response)

@app.route('/temperature/pressure')
# Function to get temperature from pressure sensor
def temp_pressure():
    temp_p = sense.get_temperature_from_pressure()
    return "Temperature: {0}".format(temp_p)

@app.route('/temperature/humidity')
# Function to get temperature from humidity sensor
def temp_humidity():
    temp_h = sense.get_temperature_from_humidity()
    return "Temperature: {0}".format(temp_h)

# Pressure route
@app.route('/pressure')
# Function to get pressure from presure sensor
def pressure():
    pressure = sense.get_pressure()
    return "Temperature: {0}".format(pressure)

# Humidity route
@app.route('/humidity')
# Function to get pressure from presure sensor
def humidty():
    humidity = sense.get_humidity()
    return "Temperature: {0}".format(humidity)

# Compass route
@app.route('/compass')
# Function to get magnetometer (compass) from magnetometer sensor
def compass():
    north = sense.get_compass()
    return "Temperature: {0}".format(north)


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

    return "Accelerometer (X,Y,Z): {0}, {1}, {2}".format(pitch_acc, roll_acc, yaw_acc)

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

    return "Gryoscope: {0}, {1}, {2}".format(pitch_gyro, roll_gyro, yaw_gyro)

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

    return "IMU: {0}, {1}, {2}".format(pitch_IMU, roll_IMU, yaw_IMU)

if __name__ =='__main__':
    app.run(debug=True)


