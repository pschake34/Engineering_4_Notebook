# Paul Schakel
# Launch Pad

import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_prev = button.value
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

def countdown(x):
    print("Starting Countdown...")
    BLINK_DURATION = 0.5
    COUNT_DURATION = 1
    LAST_COUNT = time.monotonic() - COUNT_DURATION
    LAST_BLINK_TIME = time.monotonic()
    SERVO_CHANGE = 1.23
    button_prev = False
    servo1.angle = 0
    while x >= 0:
        now = time.monotonic()
        if now >= LAST_COUNT + COUNT_DURATION and x > 0:
            print(f"{x} seconds left...")
            x -= 1
            led_red.value = True
            LAST_COUNT = now
            LAST_BLINK_TIME = now
        elif now >= LAST_COUNT + COUNT_DURATION and x == 0:
            x -= 1
        if led_red.value:
            if now >= LAST_BLINK_TIME + BLINK_DURATION:
                led_red.value = False
                LAST_BLINK_TIME = now
        if x < 3:
            if servo1.angle < 180 - SERVO_CHANGE:
                servo1.angle += SERVO_CHANGE
        if button.value:
            button_prev = button.value
        if not button.value and button_prev:
            print("Aborting...")
            led_red.value = False
            led_green.value = False
            button_prev = button.value
            return
    led_green.value = True
    led_red.value = False
    print("Liftoff!")

while True:
    if button.value:
        button_prev = button.value
    if not button.value and button_prev:
        led_green.value = False
        button_prev = button.value
        countdown(10)
