import BlynkLib
import json
import os
from datetime import datetime
from gpiozero import LED
from time import sleep, time
import random

BLYNK_AUTH = "eXHILSPsN8l1a3sybX44jSoMCQ3oZLeF"
blynk = BlynkLib.Blynk(BLYNK_AUTH)

led = LED(5)
Results_file = "ReactionResults.json" 
reaction_times = []
waiting = False
led_on_time = 0
next_time = time() + random.uniform(2, 5)

def get_rating(reaction_ms):
            if reaction_ms < 250:
                return "WOW! Perfect reactions"
            elif reaction_ms < 400:
                return "Great reflexes"
            elif reaction_ms < 600:
                return "Not bad"

            else:
                return "Too slow. Keep training"

print("REACTION TIME GAME")
print("Press the Button when LED turns on!")

def save_results(reactions_ms, rating):
    if os.path.exists(Results_file):
        with open(Results_file, "r") as f:
            data = json.load(f)
    
    else: 
        data = []

    entry = {
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S %p"),
        "Reaction Time": int(reactions_ms),
        "rating": rating
    }

    data.append(entry)
    with open(Results_file, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Results saved: {entry}")

 



@blynk.on("V0")
def handle_v0_write(value):
    global waiting, next_time, led_on_time
    button_value = value[0]
    blynk.last_activity = time()

    if button_value == "1":
        print("Button Pressed")
        if waiting: 
            reaction_ms = (time() - led_on_time) *1000
            reaction_times.append(reaction_ms)
            led.off()
            waiting = False
            blynk.virtual_write(1,0)
            next_time = time() + random.uniform(2, 5)
            blynk.virtual_write(2, int(reaction_ms))
            print(f"Reaction Time (ms): {reaction_ms:.0f} ms")
            rating = get_rating(reaction_ms)
            print(rating)
            save_results(reaction_ms, rating)
        
            print("Next round starting soon. Get ready...\n")


        else:
            print("Too early! Wait for LED to turn on")
            next_time = time() + random.uniform(2,5)

    # else: 
    #     print("Button Released")
try:
    while True:
       blynk.run()
    
       current = time()

       if not waiting and current >= next_time:
           led.on()
           waiting = True
           led_on_time = current
           blynk.virtual_write(1, 1)
           print("LED ON - press button!")
       sleep(0.01)
except KeyboardInterrupt:
    led.off()
    blynk.virtual_write(1,0)
    print("\n GAME OVER")
    if reaction_times:
        avg = sum(reaction_times) / len(reaction_times)
        best = min(reaction_times)
        print(f"Rounds Played: {len(reaction_times)}")
        print(f"Best Time: {best:.0f}ms")
        print(f"Average Reaction Time: {avg:.0f}ms")
    else:
        print("No Rounds Played")
    print("Thank you for playing")
        


