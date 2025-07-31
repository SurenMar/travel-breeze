"""bike_clf.py is the client interface for the bike classifier"""

import joblib
import os

# Unserialize model
CURRENT_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(CURRENT_DIR, 'bike_clf.pkl')
bike_clf = joblib.load(MODEL_PATH)

def predict(temp, hum, wdsp, prcp):
    features