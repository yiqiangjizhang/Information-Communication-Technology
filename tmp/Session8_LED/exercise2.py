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

# Display letter
sense.show_letter("H", red)
sleep(1)
sense.show_letter("e", blue)
sleep(1)
sense.show_letter("l", green)
sleep(1)
sense.show_letter("l", white)
sleep(1)
sense.show_letter("o", yellow)
sleep(1)

# Change background
sense.show_letter("Z", blue,red)