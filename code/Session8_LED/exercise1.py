# LED laberinth

# Import the SenseHat object from the emulator
from sense_emu import SenseHat

# Create an object
sense = SenseHat()
sense.clear()

# Define colours
green = (0, 255, 0)
black = (0,0,0)
white = (255, 255, 255)

matrix = [
    green, white, green, green, green, green, green, green,
    green, white, green, green, white, white, white, green,
    green, white, white, white, white, green, white, green,
    green, green, green, green, green, green, white, green,
    green, white, white, white, green, white, white, green,
    green, white, green, white, white, white, green, green,
    green, white, green, green, green, green, green, green,
    green, white, green, green, green, green, green, green
]

# Display on LED matrix
sense.set_pixels(matrix)

# Display letter
sense.show_letter("Z")