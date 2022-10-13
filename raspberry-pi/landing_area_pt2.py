# Paul Schakel
# Landing Area Part 2
3
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import board
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import time

# Set up OLED Screen
displayio.release_displays()

sda_pin = board.GP10
scl_pin = board.GP11
i2c = busio.I2C(scl_pin, sda_pin)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def get_input(): # Takes user input of 3 sets of coordinates
    print("Enter 3 sets of coordinates: ")
    coordinates = []
    try: # Makes sure that the user is entering the correct syntax
        for i in range(3):
            inp = input(f"Enter coordinate set {i} in x,y format: ")
            coordinate = inp.split(',') # Splits the input string into its 2 numbers
            print(coordinate)
            x = float(coordinate[0])
            y = float(coordinate[1])
            coordinates.append([x, y])
        return coordinates
    except:
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!\n\n")
        return get_input()

def draw(coordinates, area):
    # create the display group
    splash = displayio.Group()

    x = []
    y = []
    for i in range(3):
        x.append(int(coordinates[i][0] + 64))
        y.append(int(-1*coordinates[i][1] + 32))

    # Create lines for OLED
    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    vline = Line(64,0,64,64, color=0xFFFF00)
    splash.append(vline)
    circle = Circle(64, 32, 2, outline=0xFFFF00)
    splash.append(circle)
    triangle = Triangle(x[0], y[0], x[1], y[1], x[2], y[2], outline=0xFFFF00)
    splash.append(triangle)

    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=str(area)+"km2", color=0xFFFF00, x=5, y=5)
    splash.append(text_area)

    # send display group to screen
    display.show(splash)


def calculate(coordinates): # Calculates the area or a triangle from the coordinates of its vertices
    print(coordinates)
    area = 1/2*abs(coordinates[0][0] * (coordinates[1][1] - coordinates[2][1]) + coordinates[1][0] * (coordinates[2][1] - coordinates[0][1]) + coordinates[2][0] * (coordinates[0][1] - coordinates[1][1]))
    return area

while True:
    coordinates = get_input()
    area = calculate(coordinates)
    draw(coordinates, area)
    print(f"The area of the triangle with vertices ({coordinates[0][0]}, {coordinates[0][1]}), ({coordinates[1][0]}, {coordinates[1][1]}), ({coordinates[2][0]}, {coordinates[2][1]}) is {area} square km.\n\n")