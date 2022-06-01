from flask import Flask, render_template, Response

from camera import VideoCamera
from siren_script import Siren
import RPi.GPIO as GPIO
from python_code.firebase_connection import FirebaseHandling

pi_camera = VideoCamera(flip=False)  # flip pi camera if upside down.

app = Flask(__name__)


@app.route("/")
def index():
    FirebaseHandling.update_view_variable(view=True)
    return render_template("index.html")


def gen(camera):
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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
    # Siren.turn_on_siren()
    return "Turning Siren ON !"


@app.route("/siren_off/", methods=["GET"])
def siren_off():
    Siren.turn_off_siren()
    return "Turning Siren OFF !"


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=False)
