import firebase_admin
from firebase_admin import credentials, db
import os
import json

# Get the absolute path to key.json
current_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(current_dir, 'key.json')

# Load the key.json file
with open(key_path, 'r') as f:
    key_data = json.load(f)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(key_data)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://yellow-vortex-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get Firebase Realtime Database references
commands_ref = db.reference('/commands')
bpm_ref = commands_ref.child('BPM')
ECG_ref = commands_ref.child('ECG')
humidity_ref = commands_ref.child('humidity')
temperature_ref = commands_ref.child('temperature')

def set_bpm(bpm):
    bpm_ref.set({
        'average_bpm': bpm
    })

def set_ECG(ecg):
    ECG_ref.set({'average_ecg': ecg})

def set_humidity(humidity):
    humidity_ref.set(humidity)

def set_temperature(temperature):
    temperature_ref.set(temperature)

