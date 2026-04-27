import RPi.GPIO as GPIO
import time

BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print(GPIO.input(BUTTON_PIN))
    time.sleep(0.5)