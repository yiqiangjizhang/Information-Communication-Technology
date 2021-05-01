# Sense data from the SenseHat and write data to a file

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
import time # Time library
import datetime
import csv

# Create an object
sense = SenseHat()
sense.clear()

# Field Names
fieldnames = ["Temp (ºC) [Temp sensor]", "Temp (ºC) [Pressure sensor]", "Temp (ºC) [Humidity sensor]", "Pressure (mbar) [Pressure sensor]", "Humidity (mbar) [Humidity sensor]", "Pitch (º) [IMU]", "Roll (º) [IMU]", "Yaw (º) [IMU]", "Pitch (º) [Accel sensor]", "Roll (º) [Accel sensor]", "Yaw (º) [Accel sensor]", "Pitch (º) [Gyro sensor]", "Roll (º) [Gyro sensor]", "Yaw (º) [Gyro sensor]", "North (%) [Compass sensor]"]

# Create the csv file:
with open('database_3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)

    # writer.writerow(['1'])
    writer.writerow(["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"])
    writer.writerow(["2"])

# # Loop infinitely
# while True:
#     # Read temp from temperature sensor
#     temp = sense.get_temperature()
#     # Read temp from pressure sensor
#     temp_p = sense.get_temperature_from_pressure()
#     # Read temp from humidity sensor
#     temp_h = sense.get_temperature_from_humidity()
    
#     # Read pressure from pressure sensor
#     pressure = sense.get_pressure()
#     # Read humidity from humidity sensor
#     humidity = sense.get_humidity()