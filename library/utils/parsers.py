"""
A file to store parser functions for all kinds of data
"""

from numpy import isnan

def parse_weather_data(raw_data):
    """
    This function parses and returns weather data of type DateFrame
    """
    parsed_data = []
    for _, row in raw_data.iterrows():
        # Parse data only if current row if valid
        if _weather_valid(row):
            parsed_data.append({
                'temp': float(row['temp']),
                'humidity': float(row['rhum']),
                'precipitation': float(row['prcp']),
                'wind_speed': float(row['wspd']),
                'weather_code': float(row['coco']),
            })
            
    return parsed_data

def _weather_valid(row):
    """
    This helper function checks if any of the needed variables are NaNs
    """
    return not (isnan(row['temp']) or isnan(row['rhum']) or \
        isnan(row['prcp']) or isnan(row['wspd']) or isnan(row['coco']))
    
    