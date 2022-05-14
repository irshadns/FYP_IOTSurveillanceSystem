import pyrebase
import socket
from python_code.config import CONFIG, FLASK_SERVER_PORT
from time import sleep


def connect_firebase():
    firebase = pyrebase.initialize_app(CONFIG)
    database = firebase.database()
    return database


def send_dynamic_urls_to_firebase():
    prefix = "http://"
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    camera_view_url = prefix + str(ip_address) + FLASK_SERVER_PORT
    siren_on_url = prefix + str(ip_address) + FLASK_SERVER_PORT + "/siren_on/"
    siren_off_url = prefix + str(ip_address) + FLASK_SERVER_PORT + "/siren_off/"
    data = {
        "url": camera_view_url,
        "siren_on_url": siren_on_url,
        "siren_off_url": siren_off_url,
    }
    database = connect_firebase()
    sleep(1.5)
    database.child("pi_data").update(data)


send_dynamic_urls_to_firebase()
