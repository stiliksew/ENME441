import RPi.GPIO as GPIO
import time

class Shifter:
    def __init__(self, serialPin, clockPin, latchPin):
        self.serialPin=serialPin
        self.clockPin=clockPin
        self.latchPin=latchPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.serialPin, GPIO.OUT)
        GPIO.setup(self.latchPin, GPIO.OUT, initial=0) # start latch & clock low
        GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

    def shiftByte(self,b): # send a byte of data to the output
        for i in range(8):
            GPIO.output(self.serialPin, b & (1<<i))
            self.__ping(self.clockPin) # add bit to register
        self.__ping(self.latchPin) # send register to output

    def __ping(self,p): # ping the clock or latch pin
        GPIO.output(p,1)
        time.sleep(0)
        GPIO.output(p,0)
        
#shifter_obj=Shifter(23,25,24)
#shifter_obj.shiftByte(7)
        
    #GPIO.output(latchPin, 1) # ping the latch pin to send register to output
    #time.sleep(0)
    #GPIO.output(latchPin, 0)
