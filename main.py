import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

OD1 = 20 # Infrared Obstacle Avoidance Sensor 1(left side)
OD2 = 21 # Infrared Obstacle Avoidance Sensor 2(right side)
IPL1 = 2
IPL2 = 3
IPR1 = 17
IPR2 = 4

GPIO.setup(OD1, GPIO.IN)
GPIO.setup(OD2, GPIO.IN)
GPIO.setup(IPL1, GPIO.OUT)
GPIO.setup(IPL2, GPIO.OUT) 
GPIO.setup(IPR1, GPIO.OUT)
GPIO.setup(IPR2, GPIO.OUT)

def forward():
    GPIO.output(IPL1, True) # you can also use GPIO.HIGH
    GPIO.output(IPL2, False) # you can also use GPIO.LOW
    GPIO.output(IPR1, True)
    GPIO.output(IPR2, False)
    time.sleep(1)

def backward():
    GPIO.output(IPL1, False)
    GPIO.output(IPL2, True)
    GPIO.output(IPR1, False)
    GPIO.output(IPR2, True)
    time.sleep(1)

def stop():
    GPIO.output(IPL1, False)
    GPIO.output(IPL2, False)
    GPIO.output(IPR1, False)
    GPIO.output(IPR2, False)

def Left():
    GPIO.output(IPL1, False)
    GPIO.output(IPL2, True)
    GPIO.output(IPR1, True)
    GPIO.output(IPR2, False)
    time.sleep(0.5)

def Right():
    GPIO.output(IPL1, True)
    GPIO.output(IPL2, False)
    GPIO.output(IPR1, False)
    GPIO.output(IPR2, True)
    time.sleep(0.5)

try:
    while True:
        if GPIO.input(OD2) == 1 and GPIO.input(OD1) == 1:
            stop()
        else:
            forward()
            if GPIO.input(OD2):
                stop()
                backward()
                Left()
            if GPIO.input(OD1):
                stop()
                backward()
                Right()
            time.sleep(0.5)

except KeyboardInterrupt:
    stop()
    GPIO.cleanup()