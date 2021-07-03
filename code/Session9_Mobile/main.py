
# Import Flask
from flask import Flask
from sense_emu import SenseHat
from flask import jsonify
from flask import request

sense = SenseHat()
sense.clear()

# Define colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)


# Store name of the program
app = Flask(__name__)

# Route of the app is the main route of the web server
@app.route('/')
# Function
def index():
    return "Raspberry PI ICT REST Server"

# Create a new LED route
@app.route('/LED/write')
# Function to get temperature from temperature sensor
def write_message():
    msg = request.args.get('message')
    colour= request.args.get('colour')
    rgb_split = colour.split(",")
    print(rgb_split)
    rgb = (int(rgb_split(0)), int(rgb_split(1)), int(rgb_split(2)))
    print(rgb)
    # sense.show_message(msg,text_colour=rbg)


    return "Message " + msg +" printed successfully"



if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')

