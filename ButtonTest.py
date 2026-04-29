import RPi.GPIO as GPIO
import time

BUTTON = 18
GPIO.setmode(GPIO.BCM)

button = GPIO.setup(BUTTON, GPIO.IN)

print("System ready...")

while True:
    if GPIO.input(18):
        print("Button pressed!")
    

    time.sleep(0.1) 