import RPi.GPIO as GPIO


class Siren:
    @staticmethod
    def initialize_siren():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

    @classmethod
    def turn_on_siren(cls):
        cls.initialize_siren()
        GPIO.output(7, True)
        return True

    @staticmethod
    def turn_off_siren():
        GPIO.output(7, False)
        GPIO.cleanup()
