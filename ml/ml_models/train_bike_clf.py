"""train_bike_clf trains the bike suitability classifier"""

# Import ML libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier

# Import path libraries
import joblib
import os

# Get datasets and convert to df
CURRENT_DIR = os.path.dirname(__file__)
bike_csv_path = os.path.join(CURRENT_DIR, '..', 'datasets', 'bike.csv')
bike_csv_path = os.path.abspath(bike_csv_path)
bike_df = pd.read_csv(bike_csv_path)



