# Date: 04.06.21
# Desc: This web application serves a motion JPEG stream
import RPi.GPIO as GPIO
from flask import Flask, render_template, Response

from camera import VideoCamera
from firebase_connection import FirebaseHandling

pi_camera = VideoCamera(flip=False)  # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")  # you can customze index.html here


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@app.route("/video_feed")
def video_feed():
    return Response(
        gen(pi_camera), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/siren_on/", methods=["GET"])
def siren_on():
    print("Turning Siren ON !")
    print("api endpoint: /siren_on/")
    # # GPIO.setmode(GPIO.BOARD)
    # # GPIO.setup(7, GPIO.OUT)
    # # GPIO.output(7, True)
    # is_siren_on = Siren.turn_on_siren()
    # siren_control(siren=True)

    FirebaseHandling.update_firebase_notification_variable(motion_detected=False)
    pin = 13
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    return "Turning Siren ON !"


@app.route("/siren_off/", methods=["GET"])
def siren_off():
    # print("SIREN VALUE", is_siren_on)
    # # Siren.turn_off_siren()
    # GPIO.output(7, False)
    # GPIO.cleanup()
    # siren_control(siren=False)

    print("Turning Siren OFF !")
    print("api endpoint: /siren_off/")
    FirebaseHandling.update_firebase_notification_variable(motion_detected=False)
    GPIO.cleanup()
    # pin = 13
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(pin, GPIO.OUT)
    # GPIO.output(pin, False)

    return "Turning Siren OFF !"


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=False)
