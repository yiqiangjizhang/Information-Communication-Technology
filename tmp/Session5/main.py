# Create a database and add different tables

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
import time # Time library
import datetime
import csv
import sqlite3

# Create an object
sense = SenseHat()
sense.clear()

# Create database
sqlite_file = "database.db"

# Connection
conn = sqlite3.connect(sqlite_file)

# Cursor for commands and accessing information
cur = conn.cursor()

# 0=real, 1=virtual=compound

# Insert new sensors to database file
# Command to create a SENSOR table
sql = "CREATE TABLE sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, compound INTEGER)"
cur.execute(sql)

# Command to create a VARIABLES table
sql = "CREATE TABLE variables (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_id INTEGER, name TEXT NOT NULL, description TEXT, units TEXT)"
cur.execute(sql)

# Command to create a MEASURES table
sql = "CREATE TABLE measures (id INTEGER PRIMARY KEY AUTOINCREMENT, variable_id INTEGER, measure TEXT, date TEXT)"
cur.execute(sql)

# Commit the changes
conn.commit()


# Insert new sensors into table
# 1. Pressure sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Pressure', 'Pressure sensor', 0)"
cur.execute(new_sensor)

# 2. Humidity sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Humidity', 'Humidity sensor', 0)"
cur.execute(new_sensor)

# 3. Temperature sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Temperature', 'Temperature sensor', 0)"
cur.execute(new_sensor)

# 4. Magnetometer (Compass) sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Magnetometer', 'Magnetometer (Compass) sensor', 0)"
cur.execute(new_sensor)

# 5. Accelerometer sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Accelerometer', 'Accelerometer sensor', 0)"
cur.execute(new_sensor)

# 6. Gyroscope sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Gyroscope', 'Gyroscope sensor', 0)"
cur.execute(new_sensor)

# 7. IMU sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('IMU', 'IMU sensor (orientation processed by IMU)', 0)"
cur.execute(new_sensor)

# Commit the changes
conn.commit()


# Insert new variables into table
# Pressure variable from Pressure sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('1', 'Pressure','mbar')"
cur.execute(new_var)

# Temperature variable from Temperature sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('1', 'Temperature','ºC')"
cur.execute(new_var)

# Humidity variable from Humidity sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('2', 'Humidity','%rH')"
cur.execute(new_var)

# Temperature variable from Humidity sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('2', 'Temperature','ºC')"
cur.execute(new_var)

# Temperature variable from Temperature sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('3', 'Temperature','ºC')"
cur.execute(new_var)

# Magnetometer variable from Magnetometer sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('4', 'Magnetometer','% compass')"
cur.execute(new_var)

# Accelerometer (X,Y,Z) variables from Accelerometer sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('5', 'X','g')"
cur.execute(new_var)
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('5', 'Y','g')"
cur.execute(new_var)
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('5', 'Z','g')"
cur.execute(new_var)

# Gyroscope (Pitch,Roll,Yaw) variables from Gyroscope sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('6', 'Pitch','º')"
cur.execute(new_var)
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('6', 'Roll','º')"
cur.execute(new_var)
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('6', 'Yaw','º')"
cur.execute(new_var)

# IMU (Pitch,Roll,Yaw) variables from IMU sensor
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('7', 'Pitch','º')"
cur.execute(new_var)
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('7', 'Roll','º')"
cur.execute(new_var)
new_var = "INSERT INTO variables (sensor_id, name, units) VALUES ('7', 'Yaw','º')"
cur.execute(new_var)

# Commit the changes
conn.commit()


## Get measures
# NUmber of measures
n = 5

for i in range(1,n):

    # Save current beginning time
    start = time.time()

    # Read an write time
    current_time = datetime.datetime.utcnow()

    # Read pressure from pressure sensor
    pressure = sense.get_pressure()
    # Read temp from pressure sensor
    temp_p = sense.get_temperature_from_pressure()

    # Read humidity from humidity sensor
    humidity = sense.get_humidity()
    # Read temp from humidity sensor
    temp_h = sense.get_temperature_from_humidity()

    # Read temp from temperature sensor
    temp = sense.get_temperature()

    # Read magnetometer (compass) data from magnetometer sensor
    for i in range(0,10):
        compass = sense.get_compass()

    # Read accelerometer data from accelerometer sensor
    for i in range(0,10):
        accel_only = sense.get_accelerometer()
    pitch_acc = accel_only["pitch"]
    roll_acc = accel_only["roll"]
    yaw_acc = accel_only["yaw"]

    # Read gyroscope data from gyroscope sensor
    for i in range(0,10):
        gyro_only = sense.get_gyroscope()
    pitch_gyro = gyro_only["pitch"]
    roll_gyro = gyro_only["roll"]
    yaw_gyro = gyro_only["yaw"]

    # Read IMU data from IMU sensor (processed)
    for i in range(0,10):
        o = sense.get_orientation() # 'o' object is a dictionary
    pitch_IMU = o["pitch"]
    roll_IMU = o["roll"]
    yaw_IMU = o["yaw"]

    # Write Pressure measurement from Pressure sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (1, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(pressure,current_time)
    cur.execute(query)

    # Write Temperature measurement from Pressure sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (2, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(temp_p,current_time)
    cur.execute(query)

    # Write Humidity measurement from HUmidity sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (3, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(humidity,current_time)
    cur.execute(query)

    # Write Temperature measurement from Humidity sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (4, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(temp_h,current_time)
    cur.execute(query)

    # Write Temperature measurement from Temperature sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (5, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(temp,current_time)
    cur.execute(query)

    # Write Magnetometer (compass) measurement from Magnetometer sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (6, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(compass,current_time)
    cur.execute(query)

    # Write Accelerometer measurement from Accelerometer sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (7, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(pitch_acc,current_time)
    cur.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (8, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(roll_acc,current_time)
    cur.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (9, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(yaw_acc,current_time)
    cur.execute(query)

    # Write Gyroscope measurement from Gyroscope sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (10, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(pitch_gyro,current_time)
    cur.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (11, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(roll_gyro,current_time)
    cur.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (12, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(yaw_gyro,current_time)
    cur.execute(query)

    # Write IMU measurement from IMU (processed) sensor
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (13, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(pitch_IMU,current_time)
    cur.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (14, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(roll_IMU,current_time)
    cur.execute(query)
    query = "INSERT INTO measures (variable_id, measure, date) VALUES (15, {0}, '{1:%Y-%m-%d %H:%M%S.%f}')".format(yaw_IMU,current_time)
    cur.execute(query)

    # Save current end time
    end = time.time()
    elapsed_time = start - end

    # Sample sample_frequency
    sample_frequency = 1/elapsed_time
    
    # Make measurements every second
    time.sleep(1 - elapsed_time) # Sleep for 1 second taking into account the elapsed time

    # Commit the changes
    conn.commit()


# Commit the changes
conn.commit()

# Sleep for 5 seconds
time.sleep(5)

# Close connection
conn.close()



