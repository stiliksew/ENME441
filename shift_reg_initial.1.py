import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0) # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b01100110 # pattern to display

def ping(p): # ping the clock or latch pin
    GPIO.output(p,1)
    time.sleep(0)
    GPIO.output(p,0)
    
def shiftByte(b): # send a byte of data to the output
    for i in range(8):
        GPIO.output(dataPin, b & (1<<i))# checks each bit to see if they equal 1
        ping(clockPin) # add bit to register
    ping(latchPin) # send register to output
    
try:
    while 1:
        #for i in range(10):
            shiftByte(5)# convertes number to binary.
            time.sleep(0.5)
except:
    GPIO.cleanup()