# Sense data from the SenseHat

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
import time # Time library
import datetime # Date time
import csv # Import csv

# Create an object
sense = SenseHat()
sense.clear()

# Field Names
fieldnames = ["Current UTC Time","Temp (ºC) [Temp sensor]", "Temp (ºC) [Pressure sensor]", "Temp (ºC) [Humidity sensor]", "Pressure (mbar) [Pressure sensor]", "Humidity (mbar) [Humidity sensor]", "Pitch (º) [IMU]", "Roll (º) [IMU]", "Yaw (º) [IMU]", "Pitch (º) [Accel sensor]", "Roll (º) [Accel sensor]", "Yaw (º) [Accel sensor]", "Pitch (º) [Gyro sensor]", "Roll (º) [Gyro sensor]", "Yaw (º) [Gyro sensor]", "North (%) [Compass sensor]"]

# Create the csv file:
with open('database_2.csv', 'w', newline='') as file:
    # Write csv
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    
    # Infinite loop
    while True:
        # Save current beginning time
        start = time.time()

        # Read temp from temperature sensor
        temp = sense.get_temperature()
        # Read temp from pressure sensor
        temp_p = sense.get_temperature_from_pressure()
        # Read temp from humidity sensor
        temp_h = sense.get_temperature_from_humidity()
        # Read pressure from pressure sensor
        pressure = sense.get_pressure()
        # Read humidity from humidity sensor
        humidity = sense.get_humidity()
                
        # Let the sensors have enough data by measuring multiple times
        for i in range(0,10):
            o = sense.get_orientation() # 'o' object is a dictionary
        pitch_IMU = o["pitch"]
        roll_IMU = o["roll"]
        yaw_IMU = o["yaw"]

        for i in range(0,10):
            accel_only = sense.get_accelerometer()
        pitch_acc = accel_only["pitch"]
        roll_acc = accel_only["roll"]
        yaw_acc = accel_only["yaw"]

        for i in range(0,10):
            gyro_only = sense.get_accelerometer()
        pitch_gyro = gyro_only["pitch"]
        roll_gyro = gyro_only["roll"]
        yaw_gyro = gyro_only["yaw"]

        for i in range(0,10):
            north = sense.get_compass()

        # Read an write time
        current_time = datetime.datetime.utcnow()
        
        # writer.writerow(['1'])
        writer.writerow([current_time,temp,temp_p,temp_h,pressure,humidity,pitch_IMU,roll_IMU,yaw_IMU,pitch_acc,roll_acc,yaw_acc,pitch_gyro,roll_gyro,yaw_gyro,north])

        # Save current end time
        end = time.time()
        elapsed_time = start - end

        # Sample sample_frequency
        sample_frequency = 1/elapsed_time
        
        time.sleep(1 - elapsed_time) # Sleep for 1 second taking into account the elapsed time

