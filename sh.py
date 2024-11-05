import RPi.GPIO as GPIO
import time
import random
from shifter import Shifter

l=[1,2,4,8,16,32,64,128]
p=[0,1,2,3,4,5,6,7]

print(l[3])
randomval=random.choice(p)
print(l[randomval])

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(self.serialPin, GPIO.OUT)
# GPIO.setup(self.latchPin, GPIO.OUT, initial=0) # start latch & clock low
# GPIO.setup(self.clockPin, GPIO.OUT, initial=0)
shifter_obj=Shifter(23,25,24)
shifter_obj.shiftByte(randomval)
  

try:
    while 1:
        move=random.choice([-1,1])
        randomval+=move
        # if randomval==8:
        #     randomval==6
        # if randomval==-1:
        #     randomval==1
        print(l[randomval])
        shifter_obj.shiftByte(l[randomval])
        time.sleep(.5)
                
        #shifter_obj=Shifter(23,25,24)
        #for i in range(10):
         #shifter_obj=Shifter(23,25,24)# convertes number to binary.
            #time.sleep(0.5)
except:
    GPIO.cleanup()
