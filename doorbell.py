#For this project I used the active buzzer, the touch sensor, and the two-color LED (large)

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN) # Touch sensor 
GPIO.setup(16, GPIO.OUT) # Active buzzer
GPIO.setup(12, GPIO.OUT) # Two-color LED (large)


def ringAndBlink():
    for i in range (6):
        GPIO.output(12, True)
        GPIO.output(16, True)
        time.sleep(0.2)
        GPIO.output(12, False)
        GPIO.output(16, False)
        time.sleep(0.2)
    
    
while True:
    if GPIO.input(21):
        ringAndBlink()

GPIO.cleanup()
