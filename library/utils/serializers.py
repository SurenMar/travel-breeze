"""
Stores serializer functions for all types of data
"""

def serialize_weather_data(raw_data):
    """
    This function parses and returns weather data of type DataFrame
    """
    # Drop specified columns and drop all rows with a missing entries
    raw_data = raw_data.drop(
        columns=['station', 'time', 'dwpt', 'snow',
        'wdir', 'wpgt', 'pres', 'tsun'], errors='ignore',
    ).dropna(axis=0)
    
    # Parse data
    serialized_data = []
    for _, row in raw_data.iterrows():
        serialized_data.append({
            'temp': float(row['temp']),
            'humidity': float(row['rhum']),
            'precipitation': float(row['prcp']),
            'wind_speed': float(row['wspd']),
            'weather_code': float(row['coco']),
        })
    
    return serialized_data