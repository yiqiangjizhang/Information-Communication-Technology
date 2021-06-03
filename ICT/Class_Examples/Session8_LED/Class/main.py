# LED writing

# Import the SenseHat object from the emulator
from sense_emu import SenseHat

# Create an object
sense = SenseHat()
sense.clear()

# Define some colours

green = (0, 255, 0) # green
black = (0,0,0) # Black

matrix = [
    green, green, green, green, green, green, green, green,
    green, green, green, green, green, green, green, green,
    green, green, green, green, green, green, green, green,
    green, green, black, black, green, green, green, green,
    green, green, black, black, green, green, green, green,
    green, green, green, green, green, green, green, green,
    green, green, green, green, green, green, green, green,
    green, green, green, green, green, green, green, green
]

# Display on LED matrix
sense.set_pixels(matrix)
