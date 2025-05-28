"""
A file to store parser functions for all kinds of data
"""

# Parses weather data where raw_data is of type DateFrame
def parse_weather_data(raw_data):
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