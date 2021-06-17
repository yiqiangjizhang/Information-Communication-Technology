# LED laberinth

# Libraries
from sense_emu import SenseHat
from time import sleep

# Create an object
sense = SenseHat()
sense.clear()

# Define colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

while True:
    sense.show_message("Hello world!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)