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
    now = datetime.datetime.now()
    print(now)
    current_time_1 = now.strftime("%H:%M:%S")
    print("Current Time =", current_time_1)