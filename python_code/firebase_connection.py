import pyrebase
import socket
from config import CONFIG, FLASK_SERVER_PORT
from time import sleep


class FirebaseHandling:
    def __init__(self) -> None:
        firebase = pyrebase.initialize_app(CONFIG)
        database = firebase.database()
        super(FirebaseHandling, self).__init__()

    # def connect_firebase():
    #     firebase = pyrebase.initialize_app(CONFIG)
    #     database = firebase.database()
    #     return database

    def send_dynamic_urls_to_firebase(self):
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
        # database = connect_firebase()
        # sleep(1.5)
        # database.child("pi_data").update(data)
        sleep(1.5)
        self.database.child("pi_data").update(data)

    def send_initial_data(self):
        data = {
            "detection": False,
            "authenticated": False,
            "view": False,
        }
        # database = connect_firebase()
        # sleep(1.5)
        # database.child("pi_data").update(data)
        self.database.child("pi_data").update(data)

    def update_firebase_notification_variable(self, motion_detected: bool):
        data = {"detection": motion_detected}
        # database = connect_firebase()
        # sleep(1.5)
        # database.child("pi_data").update(data)
        self.database.child("pi_data").update(data)


FirebaseHandling.send_dynamic_urls_to_firebase()
FirebaseHandling.send_initial_data()
