import time

def flash_dot(led):
    led.value(1)
    time.sleep(0.15)
    led.value(0)

def flash_dash(led):
    led.value(1)
    time.sleep(0.35)
    led.value(0)

def flash_error(red, green):
    for _ in range(2):
        red.value(1)
        green.value(1)
        time.sleep(0.15)
        red.value(0)
        green.value(0)
        time.sleep(0.1)
