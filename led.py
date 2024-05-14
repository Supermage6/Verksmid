from machine import Pin
import time

# Define the LED pin
LED_PIN = 21  # GPIO pin 21 of the ESP32

# Initialize the LED pin as an output
led = Pin(LED_PIN, Pin.OUT)

# Turn off the LED initially
led.off()

# Blink the LED
while True:
    led.on()  # Turn on the LED
    time.sleep(0.1)  # Wait for 1 second
    led.off()  # Turn off the LED
    time.sleep(0.2)  # Wait for 1 second
