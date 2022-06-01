import time

import cv2
import numpy as np
from imutils.video.pivideostream import PiVideoStream


class VideoCamera(object):
    def __init__(self, flip=False):
        self.cm = PiVideoStream().start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.cm.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.cm.read())
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
