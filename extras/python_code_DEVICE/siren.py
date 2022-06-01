from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

for i in range(3):
    GPIO.output(10, GPIO.HIGH) # Turn on
    sleep(3)
    print("HIGH")# Sleep for 1 second
    GPIO.output(10, GPIO.LOW)  # Turn off
    print("LOW")
    sleep(3)
    

