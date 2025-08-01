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
from sklearn.metrics import accuracy_score

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

# Fine tune classifier
'''
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=4,
)

# Fine tune hyperparameters
param_grid = {
    'n_estimators': [180, 200, 220],
    'max_depth': [11, 13, 15],
    'min_samples_split': [2, 4, 6],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [False, True]
}
grid = GridSearchCV(
    estimator=RandomForestClassifier(random_state=4),
    param_grid=param_grid,
    scoring='accuracy',
    cv=5,
    n_jobs=2,
    error_score='raise',
)

grid.fit(X_train, y_train)
y_pred = grid.best_estimator_.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(grid.best_params_)
print(f'Scoring: {grid.best_score_:.4f}')
print(f'Accuracy: {accuracy:.4f}')
'''

# Train rf classifier based on best params from grid search
forest = RandomForestClassifier(
    n_estimators=200,
    max_depth=13,
    min_samples_leaf=1,
    min_samples_split=4,
    max_features='sqrt',
    bootstrap=True,
    n_jobs=2,
    random_state=4
)

# Fit on all data
forest.fit(X, y)

# Fit and serialize model
joblib.dump(forest, 'library/ml/ml_models/bike_clf.pkl')
