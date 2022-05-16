from time import sleep
import RPi.GPIO as GPIO
from firebase_connection import FirebaseHandling


class MotionSensorNotifier:
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        self.pir_pin = 26
        GPIO.setup(self.pir_pin, GPIO.IN)
        self.motion_detected = False
        super(MotionSensorNotifier, self).__init__()

    def send_notifier(self):
        is_motion_detected = self.motion_detected
        FirebaseHandling.update_firebase_notification_variable(
            motion_detected=is_motion_detected
        )
        self.motion_detected = False


motion_sensor = MotionSensorNotifier()
while True:
    try:
        GPIO.add_event_detect(
            motion_sensor.pir_pin, GPIO.RISING, callback=motion_sensor.send_notifier()
        )
        sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
