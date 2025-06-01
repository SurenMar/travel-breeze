"""
A file containing functions used to store processed data into database
"""

from library.models import Destination, MonthlyWeather

def save_destination(user, country, city, lat, lon):
    """
    A function that saves data to Destination model
    """
    # Create destination instance with given inputs
    destination = Destination.objects.create(
        owner = user,
        country = country,
        city = city,
        latitude = lat,
        longitude = lon,
    )
    return destination.pk   # Return primary key to store monthly data

def save_monthly_weather(destination_pk, weather_data):
    """
    A function that saves data to MonthlyWeather model
    """
    # Get destination corrosponding to given primary key
    destination = Destination.objects.get(id=destination_pk)
    MONTHS = 12
    
    # Create 12 instances, 1 for each month, all belonging to same destination
    for month in range(MONTHS):
        MonthlyWeather.objects.create(
            destination = destination,
            month = weather_data[month]['month'],
            avg_temp = round(weather_data[month]['avg_temp'], 1),
            max_temp = round(weather_data[month]['max_temp'], 1),
            min_temp = round(weather_data[month]['min_temp'], 1),
            humidity = round(weather_data[month]['humidity'], 1),
            precipitation = int(weather_data[month]['precipitation']),
            wind_speed = round(weather_data[month]['wind_speed'], 1),
            weather_condition = weather_data[month]['weather_condition'],
        )