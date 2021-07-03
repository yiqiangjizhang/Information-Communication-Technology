# Sense data from the SenseHat

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
import time # Time library
import datetime

# Create an object
sense = SenseHat()

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
    
    # Print temp data
    print("Temperature from pressure sensor: {0:3f} ºC; from humidity is {1:3f} ºC".format(temp_p,temp_h))
    # Print pressure and humidity data
    print("Pressure is: {0:0f} mbar".format(pressure))
    print("Humidity is: {0:0f} %".format(humidity))
    
    # Let the sensors have enough data by measuring multiple times
    for i in range(0,10):
        o = sense.get_orientation() # 'o' object is a dictionary
    print(o)

    # Read an write time
    current_time = datetime.datetime.now()
    print(current_time)
    
    # Save current end time
    end = time.time()
    elapsed_time = start - end
    time.sleep(1 - elapsed_time) # Sleep for 1 second taking into account the elapsed time

