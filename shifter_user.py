import RPi.GPIO as GPIO
import time
from shifter import Shifter

shifter_obj=Shifter(23,24,25)


try:
    while 1:
        #for i in range(10):
            shifter_obj.shiftByte(78)# convertes number to binary.
            #time.sleep(0.5)
except:
    GPIO.cleanup()