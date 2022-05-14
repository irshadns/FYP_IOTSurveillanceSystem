import pyrebase
from .config import CONFIG

def connect_firebase():
    firebase = pyrebase.initialize_app(CONFIG)
    database = firebase.database()
    return database
