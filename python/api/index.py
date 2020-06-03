import pyrebase
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

config = {
    "apiKey": os.getenv("ENV_API_KEY"),
    "authDomain": os.getenv("ENV_AUTH_DOMAIN"),
    "databaseURL": os.getenv("ENV_DATABASE_URL"),
    "storageBucket": os.getenv("ENV_STORAGE_BUCKET")
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# data = {"station_name": "chui 4", "station_id": 266}

db.child("stations").push(data)
