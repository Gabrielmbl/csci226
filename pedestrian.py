import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

while True:
    if GPIO.input(19):
        time.sleep(4)
        GPIO.output(18, False)
        GPIO.output(23, True)
        print("YELLOW")
        time.sleep(4)
        GPIO.output(23, False)
        GPIO.output(12, True)
        print("RED")
        time.sleep(10)
        for i in range(3):
            GPIO.output(12, False)
            time.sleep(0.5)
            GPIO.output(12, True)
            time.sleep(0.5)
        for i in range (6):
            GPIO.output(12, False)
            time.sleep(0.2)
            GPIO.output(12, True)
            time.sleep(0.2)
        for i in range(15):
            GPIO.output(12, True)
            time.sleep(0.07)
            GPIO.output(12, False)
            time.sleep(0.07)
            
    else:
        GPIO.output(18, True)
        GPIO.output(23, False)
        GPIO.output(12, False)
        print("GREEN")
        time.sleep(0.1)
        
        
GPIO.cleanup()
    