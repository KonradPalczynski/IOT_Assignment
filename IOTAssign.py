import RPi.GPIO as GPIO
import time
import random
import json

# GPIO setup
LED_PIN = 18
BUTTON_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Reaction Time System Started")
print("Wait for the LED...")

try:
    while True:
        # Random delay before LED turns on
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)

        # Turn LED ON
        GPIO.output(LED_PIN, GPIO.HIGH)
        start_time = time.time()

        # Wait for button press
        while GPIO.input(BUTTON_PIN) == GPIO.LOW:
            pass

        reaction_time = time.time() - start_time

        # Turn LED OFF
        GPIO.output(LED_PIN, GPIO.LOW)

        # Create data (JSON format for IoT requirement)
        data = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "reaction_time": round(reaction_time, 3)
        }

        print("Reaction Time:", data["reaction_time"], "seconds")
        print("Data:", json.dumps(data))

        # Small delay before next round
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()