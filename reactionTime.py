# from gpiozero import LED
# from time import sleep 

# led = LED(5)

# while True:
#     led.on()
#     print("LED ON")
#     sleep(1)

#     led.off()
#     print("LED OFF")
#     sleep(1)

# @blynk.on("V0")
# def blynk_v0_write(value):
#     global waiting

#     print("Button:", value)

#     if value[0] == "1" and waiting:
#         print("REACTION DETECTED")
#         led.off()
#         waiting = False

#     else: 
#         print("Too early!")

import BlynkLib
from gpiozero import LED
from time import sleep, time
import random

BLYNK_AUTH = "eXHILSPsN8l1a3sybX44jSoMCQ3oZLeF"
blynk = BlynkLib.Blynk(BLYNK_AUTH)

led = LED(5)

waiting = False
led_on_time = 0
next_time = time() + random.uniform(2, 5)

print("Program started")


 



@blynk.on("V0")
def handle_v0_write(value):
    button_value = value[0]
    blynk.last_activity = time()
    print(f'Current button value: {button_value}')

    if button_value == "1":
        print("Button Pressed")
    else:
        print("Awaiting Press")

while True:
    blynk.run()
    
    current = time()

    if not waiting and current >= next_time:
        led.on()
        waiting = True
        led_on_time = current
        print("LED ON - press button!")

    if not waiting and current >= next_time:
        next_time = current + random.uniform(2, 5)

    sleep(0.01)
