# Joystick

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


# Loop forever
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)

        if event.action == "pressed":
      
            # Check which direction
            if event.direction == "up":
                sense.show_letter("U")      # Up arrow
            elif event.direction == "down":
                sense.show_letter("D")      # Down arrow
            elif event.direction == "left": 
                sense.show_letter("L")      # Left arrow
            elif event.direction == "right":
                sense.show_letter("R")      # Right arrow
            elif event.direction == "middle":
                sense.show_letter("M")      # Enter key
            
            # Wait a while and then clear the screen
            sleep(0.5)
            sense.clear()

