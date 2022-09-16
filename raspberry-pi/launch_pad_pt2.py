# Paul Schakel
# Launch Pad part 2

import board
import time
import digitalio

# Initialize variables for LEDs
led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT

def countdown(x): # count down from x to 0
    print("Starting Countdown...")
    while x > 0:
        print(f"{x} seconds left...")
        x -= 1

        # Turn LED on and off
        led_red.value = True
        time.sleep(.5)
        led_red.value = False
        time.sleep(.5)
    print("Liftoff!")
    led_green.value = True
