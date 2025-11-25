import machine
import time
from morse_logic import classify_press
from led_feedback import flash_dot, flash_dash, flash_error

# Pin definitions
KEY_PIN = 14
RED_LED = 15
GREEN_LED = 16

key = machine.Pin(KEY_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
red_led = machine.Pin(RED_LED, machine.Pin.OUT)
green_led = machine.Pin(GREEN_LED, machine.Pin.OUT)

# Timing thresholds (ms)
DOT_MAX = 200
DASH_MIN = 201

press_start = None
pressed = False

while True:
    if key.value() == 0 and not pressed:
        pressed = True
        press_start = time.ticks_ms()

    if key.value() == 1 and pressed:
        pressed = False
        duration = time.ticks_diff(time.ticks_ms(), press_start)

        symbol = classify_press(duration)

        if symbol == ".":
            flash_dot(green_led)
        elif symbol == "-":
            flash_dash(red_led)
        else:
            flash_error(red_led, green_led)

    time.sleep_ms(5)
