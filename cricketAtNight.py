#!/usr/bin/env python3
# Written by Limor "Ladyada" Fried for Adafruit Industries, (c) 2015
# This code is released into the public domain
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    
    GPIO.output(cspin, True) # set CS high (if not already high)
    GPIO.output(clockpin, False) # start clock low
    GPIO.output(cspin, False) # bring CS low

    commandout = adcnum
    commandout |= 0x18 # start bit + single-ended bit
    commandout <<= 3 # we only need to send 5 bits here

    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
            
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
    
    adcout = 0

    # read in one empty bit, one null bit and 10 ADC bits

    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)
    adcout >>= 1 # drop the last bit, i.e. the stop bit
                 # the start bit is 0 so we can ignore it
    return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler

SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

VREF = 3.3

adc = 7
value = readadc(adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
print( "ACD #{}".format( adc ) )
print( " Reading: {}".format( value ) )
print( " Voltage: {}".format( VREF * value/1023 ) )

GPIO.setup(21, GPIO.OUT) #Active Buzzer

def cricketNoise(): #Simulating a cricket 
    GPIO.output(21, True)
    time.sleep(0.08)
    GPIO.output(21, False)
    time.sleep(0.08)
    GPIO.output(21, True)
    time.sleep(0.035)
    GPIO.output(21, False)
    time.sleep(0.7)
    time.sleep(1)
    GPIO.output(21, False)

while True:
    value = readadc(adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    print( "ACD #{}".format( adc ) )
    print( " Reading: {}".format( value ) )
    print( " Voltage: {}".format( VREF * value/1023 ) )
        
    if (value > 500): #If it is dark
            cricketNoise()
    else:
        print("It is still day-time")
        time.sleep(3)

    
GPIO.cleanup()