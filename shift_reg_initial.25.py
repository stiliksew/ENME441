import RPi.GPIO as GPIO
import time

class Shifter:
    def__init__(self, serialPin, clockPin, latchPin):
        self.serialPin=dataPin
        self.clockPin=clockPin
        self.latchPin=latchPin
        
GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0) # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b00000001 # pattern to display

def shiftByte(self,b): # send a byte of data to the output
    for i in range(8):
        GPIO.output(dataPin, b & (1<<i))
        ping(clockPin) # add bit to register
    ping(latchPin) # send register to output

    def __ping(self,p): # ping the clock or latch pin
        GPIO.output(p,1)
        time.sleep(0)
        GPIO.output(p,0)
        
    GPIO.output(latchPin, 1) # ping the latch pin to send register to output
    time.sleep(0)
    GPIO.output(latchPin, 0)
try:
    while 1: pass
except:
    GPIO.cleanup()