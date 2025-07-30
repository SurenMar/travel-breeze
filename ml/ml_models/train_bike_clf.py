"""train_bike_clf trains the bike suitability classifier"""

# Import libraries for ML
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Import path libraries
import joblib
import os

# Get datasets and convert to df
CURRENT_DIR = os.path.dirname(__file__)
bike_csv_path = os.path.join(CURRENT_DIR, '..', 'datasets', 'bike.csv')
bike_csv_path = os.path.abspath(bike_csv_path)
bike_df = pd.read_csv(bike_csv_path)


bike_ddf = bike_df.dropna(axis=0)

# Average bikers between 2 and 5pm are similar, so no third party variables
#   such as time of day will affect our model
bike_df = bike_df[(bike_df['hr'] >= 14) & (bike_df['hr'] <= 17)]

# Note: We keep casual users because registered users are those who bike
#   for communiting (to work, school, etc), not for leasure.
bike_df = bike_df.drop(columns=['instant', 'dteday', 'season', 'yr', 'mnth', 
        'holiday', 'weekday', 'workingday', 'weathersit', 'atemp', 'registered', 
        'cnt', 'hr'])

# Create label column
cutoff = int(bike_df['casual'].mean())
bike_df['casual'] = np.where(bike_df['casual'] >= cutoff, 1, 0)
bike_df = bike_df.rename(columns={'casual': 'biking_suitability'})

# Preprocess features and labels
X = bike_df.drop(columns=(['biking_suitability']))
y = bike_df['biking_suitability']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=4,
)
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.fit_transform(X_test)





