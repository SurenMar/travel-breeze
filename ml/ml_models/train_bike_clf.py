"""train_bike_clf trains the bike suitability classifier"""

import pandas as pd
import numpy as np
import joblib
import os

# Data analysis libraries
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve

# ML libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# Get datasets and convert to df
CURRENT_DIR = os.path.dirname(__file__)
bike_csv_path = os.path.join(CURRENT_DIR, '..', 'datasets', 'bike_weather.csv')
bike_csv_path = os.path.abspath(bike_csv_path)
bike_df = pd.read_csv(bike_csv_path).dropna(axis=0)

# Average biker count between 12 and 2pm are similar, so no third party variables
#   such as time of day will affect our model
bike_df = bike_df[(bike_df['Hour'] >= 12) & (bike_df['Hour'] <= 14)]

# Combine Rainfall and Snowfall under single Precipitation column
MM_TO_CM = 10
bike_df = bike_df.rename(columns={'Rainfall': 'Precipitation'})
bike_df['Precipitation'] = np.where(
    bike_df['Precipitation'] > bike_df['Snowfall'] * MM_TO_CM,
    bike_df['Precipitation'], bike_df['Snowfall']) * MM_TO_CM

# Drop unnecessary columns
bike_df = bike_df.drop(columns=['Date', 'Hour', 'Visibility', 'Dew point temperature', 'Solar Radiation', 
        'Holiday', 'Seasons', 'Functioning Day', 'Snowfall'])

# Create the label column
cutoff = int(bike_df['Rented Bike Count'].median())
bike_df['Rented Bike Count'] = np.where(bike_df['Rented Bike Count'] >= cutoff, 1, 0)
bike_df = bike_df.rename(columns={'Rented Bike Count': 'biking_suitability'})

# Create features and labels
X = bike_df.drop(columns=(['biking_suitability'])).values
y = bike_df['biking_suitability'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=4,
)

# Fine tune hyperparameters
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 12, 14],
    'min_samples_split': [2, 5, 7],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt'],
    'bootstrap': [False]
}
grid = GridSearchCV(
    estimator=RandomForestClassifier(random_state=4),
    param_grid=param_grid,
    scoring='accuracy',
    cv=5,
    n_jobs=3,
    error_score='raise',
)

grid.fit(X_train, y_train)
forest = grid.best_estimator_
