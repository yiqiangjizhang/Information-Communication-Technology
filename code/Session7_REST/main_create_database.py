# Create a database and add different tables

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
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
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Pressure_sensor', 'Pressure sensor', 0)"
cur.execute(new_sensor)

# 2. Humidity sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Humidity_sensor', 'Humidity sensor', 0)"
cur.execute(new_sensor)

# 3. Temperature sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Temperature_sensor', 'Temperature sensor', 0)"
cur.execute(new_sensor)

# 4. Magnetometer (Compass) sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Magnetometer_sensor', 'Magnetometer (Compass) sensor', 0)"
cur.execute(new_sensor)

# 5. Accelerometer sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Accelerometer_sensor', 'Accelerometer sensor', 0)"
cur.execute(new_sensor)

# 6. Gyroscope sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('Gyroscope_sensor', 'Gyroscope sensor', 0)"
cur.execute(new_sensor)

# 7. IMU sensor
new_sensor = "INSERT INTO sensors (name, description, compound) VALUES ('IMU_sensor', 'IMU sensor (orientation processed by IMU)', 0)"
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

# Close connection
conn.close()
