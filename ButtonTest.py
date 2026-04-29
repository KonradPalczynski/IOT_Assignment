import RPi.GPIO as GPIO
import time

BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
button = GPIO.setup(BUTTON, GPIO.IN)

print("System ready...")

while True:
    print(GPIO.input(BUTTON_PIN))
    time.sleep(0.5)