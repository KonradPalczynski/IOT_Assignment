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

print("REACTION TIME GAME")
print("Press the Button when LED turns on!")


 



@blynk.on("V0")
def handle_v0_write(value):
    global waiting, next_time, led_on_time
    button_value = value[0]
    blynk.last_activity = time()
    #print(f'Current button value: {button_value}')

    if button_value == "1":
        print("Button Pressed")
        if waiting: 
            reaction_ms = (time() - led_on_time) *1000
            led.off()
            waiting = False
            blynk.virtual_write(1,0)
            next_time = time() + random.uniform(2, 5)
            blynk.virtual_write(2, int(reaction_ms))
            print(f"Reaction Time (ms): {reaction_ms:.0f} ms")
            if reaction_ms < 250:
                print("WOW! Perfect reactions")
            elif reaction_ms < 400:
                print("Great reflexes")
            elif reaction_ms < 600:
                print("Not bad")

            else:
                print("Too slow. Keep training")
            print("Next round starting soon. Get ready...\n")


        else:
            print("Too early! Wait for LED to turn on")
            next_time = time() + random.uniform(2,5)

    else: 
        print("Button Released")

while True:
    blynk.run()
    
    current = time()

    if not waiting and current >= next_time:
        led.on()
        waiting = True
        led_on_time = current
        blynk.virtual_write(1, 1)
        print("LED ON - press button!")

    if not waiting and current >= next_time:
        next_time = current + random.uniform(2, 5)

    sleep(0.01)
