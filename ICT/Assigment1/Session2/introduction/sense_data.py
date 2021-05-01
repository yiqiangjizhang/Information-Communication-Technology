# Sense data from the SenseHat

# More documentation: https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
import time # Time library

# Create an object
sense = SenseHat()

# Infinite loop
while True:
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
    time.sleep(1) # Read data every second
    


