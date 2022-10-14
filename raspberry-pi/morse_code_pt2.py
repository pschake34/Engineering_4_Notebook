# Paul Schakel
# Morse Code Part 1

import board
import digitalio
import time

# Initialize LED
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

# Timings for transmission
modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

while True:
    to_translate = input("Enter the phrase you would like translated: ")
    if to_translate == "-q": # Quit the program
        break
    translated = ""
    for char in to_translate: # Loop through message
        if char == " ": # Add "/" between words
            translated += "/"
        else:
            translated += MORSE_CODE[char.upper()] + " " # Translate character to morse code
    print(translated + "\n\n")

    for char in translated: # Flash LED to transmit morse code message
        if char == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(between_taps)
        elif char == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(between_taps)
        elif char == " ":
            time.sleep(between_letters)
        elif char == "/":
            time.sleep(between_words - between_letters)
        else:
            print("Error")
