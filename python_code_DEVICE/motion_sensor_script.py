import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pirPin = 26

GPIO.setup(pirPin, GPIO.IN)

def lights(pirPin):
    print("MOTION DETECTED")
    print("Lights ON")

    time.sleep(2)
    #print("MOTION DETECTED")
    print("Lights OFF")

print("READYYYY")
try:
    GPIO.add_event_detect(pirPin, GPIO.RISING, callback=lights)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()