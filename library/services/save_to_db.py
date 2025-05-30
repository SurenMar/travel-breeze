"""
A file containing functions used to store processed data into database
"""

from library.models import Destination, MonthlyWeather
from django.contrib.auth.models import User # testing purposes

def save_destination(user, country, city):
    """
    A function that saves data to Destination model
    """
    
    # Create destination instance with given inputs
    destination = Destination.objects.create(
        owner = user,
        country = country,
        city = city
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
            avg_temp = weather_data[month]['avg_temp'],
            max_temp = weather_data[month]['max_temp'],
            min_temp = weather_data[month]['min_temp'],
            humidity = weather_data[month]['humidity'],
            precipitation = weather_data[month]['precipitation'],
            wind_speed = weather_data[month]['wind_speed'],
            weather_code = weather_data[month]['weather_code'],
        )