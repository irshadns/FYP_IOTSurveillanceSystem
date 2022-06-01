import pyrebase
import socket
from config import CONFIG, FLASK_SERVER_PORT
from time import sleep


class FirebaseHandling:
    firebase = pyrebase.initialize_app(CONFIG)
    database = firebase.database()

    @classmethod
    def send_dynamic_urls_to_firebase(cls):
        prefix = "http://"
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        base_url = prefix + str(ip_address) + FLASK_SERVER_PORT + "/"
        siren_on_url = base_url + "siren_on/"
        siren_off_url = base_url + "siren_off/"
        data = {
            "url": base_url,
            "siren_on_url": siren_on_url,
            "siren_off_url": siren_off_url,
        }
        sleep(1.5)
        cls.database.child("pi_data").update(data)

    @classmethod
    def send_initial_data(cls):
        data = {
            "detection": False,
            # "authenticated": False,
            "view": False,
        }
        cls.database.child("pi_data").update(data)

    @classmethod
    def update_firebase_notification_variable(cls, motion_detected: bool):
        data = {"detection": motion_detected}
        cls.database.child("pi_data").update(data)
        
    @classmethod
    def update_view_and_motion_variable(cls, view:bool, motion_detection:bool):
        data = {
            "detection": motion_detection,
            "view": view,
        }
        cls.database.child("pi_data").update(data)
    

FirebaseHandling.send_dynamic_urls_to_firebase()
FirebaseHandling.send_initial_data()
