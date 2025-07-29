"""train_bike_clf trains the bike suitability classifier"""

# Import libraries for ML
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
import matplotlib.pyplot as plt

# Import path libraries
import joblib
import os

# Get datasets and convert to df
CURRENT_DIR = os.path.dirname(__file__)
bike_csv_path = os.path.join(CURRENT_DIR, '..', 'datasets', 'bike.csv')
bike_csv_path = os.path.abspath(bike_csv_path)
bike_df = pd.read_csv(bike_csv_path)


bike_df.dropna(axis=0)

# Note: We keep casual users because registered users are those who bike
#   for communiting (to work, school, etc), not for leasure.
bike_df.drop(['instant', 'dteday', 'season', 'yr', 'mnth', 'holiday',
        'weekday', 'workingday', 'weathersit', 'atemp', 'registered', 'cnt'], 
        axis=1)

# Average bikers between 2 and 5pm are similar, so no third party variables
#   such as time of day will affect our model
bike_df = bike_df[(bike_df['hr'] >= 14) & (bike_df['hr'] <= 17)]




