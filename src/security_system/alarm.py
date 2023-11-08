import time
import RPi.GPIO as GPIO

def trigger_alarm():
    try:
        # Initialize the GPIO library
        GPIO.setmode(GPIO.BCM)

        # Initialize the buzzer (configure the GPIO pin)
        buzzer_pin = 17  # Replace with the actual GPIO pin you're using
        GPIO.setup(buzzer_pin, GPIO.OUT)

        # Turn on the buzzer for a few seconds
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(3)  # Adjust the duration as needed
        GPIO.output(buzzer_pin, GPIO.LOW)
    finally:
        # Clean up GPIO settings
        GPIO.cleanup()
