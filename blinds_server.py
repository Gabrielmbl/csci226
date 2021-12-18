#!/usr/bin/env python3
# Written by Limor "Ladyada" Fried for Adafruit Industries, (c) 2015
# This code is released into the public domain

# from https://wiki.python.org/moin/UdpCommunication
# modified by RG Willhoft, 2020
# modified by Gabriel Lucena, 2021

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


GPIO.setup(19, GPIO.OUT) #RED LED simulating closing
GPIO.setup(13, GPIO.OUT) #GREEN LED simulating opening


def auto(adc, SPICLK, SPIMOSI, SPIMISO, SPICS):
    value = readadc(adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    print( "ACD #{}".format( adc ) )
    print( " Reading: {}".format( value ) )
    print( " Voltage: {}".format( VREF * value/1023 ) )

    if (value > 500): #If it is dark
        print("It is dark out, save energy by keeping the heat in")
        GPIO.output(13, False)
        time.sleep(1.5)
        GPIO.output(19, True)
        print("Blinds are closed")
        time.sleep(3)
    else:
        print("It is still day-time, save energy by letting natural light in")
        GPIO.output(19, False)
        time.sleep(1.5)
        GPIO.output(13, True)
        print("Blinds are open")
        time.sleep(3)

    time.sleep(1)


def openBlinds():
    GPIO.output(19, True)
    time.sleep(1.5)
    GPIO.output(19, False)
    time.sleep(0.5)
    GPIO.output(13, True)


def closeBlinds():
    GPIO.output(13, True)
    time.sleep(1.5)
    GPIO.output(13, False)
    time.sleep(0.5)
    GPIO.output(19, True)



import socket

UDP_PORT = 5004

# opens a port to listen for UDP messages
sock = socket.socket( socket.AF_INET,    # Internet
                      socket.SOCK_DGRAM) # UDP

sock.connect(('10.255.255.255', 1))
ip_addr = sock.getsockname()[0]
sock.detach()

sock = socket.socket( socket.AF_INET,    # Internet
                      socket.SOCK_DGRAM) # UDP
print("Open socket")
sock.bind((ip_addr, UDP_PORT))

while True:
    # wait for and receive message
    print("Waiting for datagram...")
    data, addr = sock.recvfrom(1024) # 1024 byte buffer

    # process message
    ip = addr[0]
    port = addr[1]
    message = data.decode("UTF-8")
    msg = message
    print("From: {}:{} - {}".format(ip,port,message))

    # Send modified message back to sender
    data = message.upper().encode("UTF-8")
    sock.sendto( data, addr )
    
    
    if msg == 'auto':
        auto(adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
            
    elif msg == 'open':
        print("Opening")
        GPIO.output(13, False)
        openBlinds()
        
    elif msg == 'close':
        print("Closing")
        GPIO.output(19, False)
        closeBlinds()
        
            
        






