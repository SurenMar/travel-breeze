"""bike_clf.py is the client interface for the bike classifier"""
import numpy as np
import joblib
import os

# Unserialize model
CURRENT_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(CURRENT_DIR, 'bike_clf.pkl')
bike_clf = joblib.load(MODEL_PATH)

def predict(temp, hum, wdsp, prcp):
    data = [temp, hum, wdsp, prcp]
    X = np.array(data).reshape(1, -1)
    return int(bike_clf.predict(X)[0])

print(predict(8.5, 75, 5.8, 0.236))