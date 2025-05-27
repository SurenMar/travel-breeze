# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Hourly, Point
#import json

# Set time period
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)

def get_weather_data(lat, lon):
    """
    A function that gets a years worth of hourly weather data based on 
    latitude and longitude input
    """
    location = Point(lat, lon)
    data = Hourly(location, start, end)
    return data.fetch()

#with open('data.json', 'w') as file:
#    json.dump(data.to_dict(orient='records'), file, indent=4)

# to update database, use .get('field') to retrieve values.
# do this in the same weather_api file by importing your model (class)
    