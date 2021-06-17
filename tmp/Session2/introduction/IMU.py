# Read IMU data from the SenseHat

# More info: https://pythonhosted.org/sense-hat/api/

# Import the SenseHat object from the emulator
from sense_emu import SenseHat
import time # Time library

# Create an object
sense = SenseHat()
sense.clear()

# Loop infinitely
while True:
    # Get IMU data
    o = sense.get_orientation() # 'o' object is a dictionary
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    # Print the whole dictionary
    print(o)
    print(pitch)
    print(roll)
    print(yaw)
    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))

    # Get accelerometer raw data
    accel = sense.get_accelerometer_raw()
    print(accel)
    accel2 = sense.get_accelerometer()
    print(accel2)

    # Get gyroscope raw data
    gyro = sense.get_gyroscope_raw()
    print(accel)

    # Get compass raw data
    compass = sense.get_compass_raw()
    print(compass)