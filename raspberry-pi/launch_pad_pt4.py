# Paul Schakel
# Launch Pad part 4

import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

# Initialize LED variables
led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT

# Initialize button variables
button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_prev = button.value

# Initialize servo variables
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

def countdown(x): # Count down from 10 to zero while blinking an LED - turns servo at 3 seconds
    print("Starting Countdown...")

    # Define some variables for time.monotonic() delays
    BLINK_DURATION = 0.5
    COUNT_DURATION = 1
    LAST_COUNT = time.monotonic() - COUNT_DURATION
    LAST_BLINK_TIME = time.monotonic()
    SERVO_CHANGE = 1.23
    button_prev = False
    servo1.angle = 0
    
    while x >= 0:
        now = time.monotonic()
        if now >= LAST_COUNT + COUNT_DURATION and x > 0: # Manage timing for counter, print to serial and turn LED on
            print(f"{x} seconds left...")
            x -= 1
            led_red.value = True
            LAST_COUNT = now
            LAST_BLINK_TIME = now
        elif now >= LAST_COUNT + COUNT_DURATION and x == 0: # Don't print if x == 0 
            x -= 1
        if led_red.value: # Turn LED off after short period of time
            if now >= LAST_BLINK_TIME + BLINK_DURATION:
                led_red.value = False
                LAST_BLINK_TIME = now
        if x < 3: # Start moving servo from 0 to 180
            if servo1.angle < 180 - SERVO_CHANGE:
                servo1.angle += SERVO_CHANGE
        if button.value: # Debounce button
            button_prev = button.value
        if not button.value and button_prev: # Abort launch
            print("Aborting...")
            led_red.value = False
            led_green.value = False
            button_prev = button.value
            return
    led_green.value = True
    led_red.value = False
    print("Liftoff!")

while True:
    if button.value: # Debounce button
        button_prev = button.value
    if not button.value and button_prev: # Start countdown
        led_green.value = False
        button_prev = button.value
        countdown(10)
