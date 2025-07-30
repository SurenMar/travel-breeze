"""
A file to store parser functions for all kinds of data
"""

from numpy import isnan

def parse_weather_data(raw_data):
    """
    This function parses and returns weather data of type DataFrame
    """
    # Drop specified columns and drop all rows with a missing entries
    raw_data = raw_data.drop(
        columns=['station', 'time', 'dwpt', 'snow',
        'wdir', 'wpgt', 'pres', 'tsun'], errors='ignore',
    ).dropna(axis=0)
    
    # Parse data
    parsed_data = []
    for _, row in raw_data.iterrows():
        parsed_data.append({
            'temp': float(row['temp']),
            'humidity': float(row['rhum']),
            'precipitation': float(row['prcp']),
            'wind_speed': float(row['wspd']),
            'weather_code': float(row['coco']),
        })
    
    return parsed_data