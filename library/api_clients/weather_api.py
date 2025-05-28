"""
A file to request an API call for weather_data
"""

# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Hourly, Point, Stations

# Set time period
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)

def get_weather_data(lat, lon):
    """
    A function that gets a years worth of hourly weather data based on
    latitude and longitude input
    """
    # Fetch weather data based on lat and lon point
    location = Point(lat, lon)
    data = Hourly(location, start, end).fetch()
    
    # Return data if information was found
    if not data.empty:
        return data
    
    # Find data through 5 nearest stations if above fails
    stations = Stations().nearby(lat, lon).fetch(5)

    for idx, row in stations.iterrows():
        # Return data if information was found
        data = Hourly(idx, start, end).fetch()
        if not data.empty:
            return data
    
    # If this is reached, None will be returned
    return data
    
    