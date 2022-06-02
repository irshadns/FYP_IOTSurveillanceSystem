import time
import RPi.GPIO as GPIO
from firebase_connection import FirebaseHandling


# class MotionSensorNotifier():
# def __init__(self) -> None:
#     GPIO.setmode(GPIO.BCM)
#     pirPin = 26
#     GPIO.setup(pirPin, GPIO.IN)

# def update_firebase_notification_variable():
#     FirebaseHandling.update_firebase_notification_variable(motion_detected=True)


GPIO.setmode(GPIO.BCM)
pirPin = 26
GPIO.setup(pirPin, GPIO.IN)
motion_times_detected = 0


def motion_detection(pirPin):
    global motion_times_detected
    motion_times_detected += 1
    print("Motion Variable ", motion_times_detected)
    if motion_times_detected > 2:
        FirebaseHandling.update_firebase_notification_variable(motion_detected=True)
        motion_times_detected = 0


while True:
    try:
        GPIO.add_event_detect(pirPin, GPIO.RISING, callback=motion_detection)
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
