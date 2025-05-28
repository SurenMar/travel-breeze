from django.shortcuts import render
from django.http import JsonResponse

# Import api clients
from library.api_clients.weather_api import get_weather_data
from library.api_clients.country_api import get_country_data

# Import utils
from library.utils.parsers import parse_weather_data

# Import services
#from library.services.save_to_db import "filename"

def world_map(request):
    context = {'title': 'Explore'}
    return render(request, 'explore/world_map.html', context)

def save_data(request):
    """
    A view which gets data, parses it, and stores in database
    """
    # Get latitude and longitude from user click
    lat = float(request.GET.get('latitude'))
    lon = float(request.GET.get('longitude'))
    
    # Get weather data through API call and parse it
    data = get_weather_data(lat, lon)
    data = parse_weather_data(data)
    
    # Get country and city name through API (no need to parse)
    country, city = get_country_data(lat, lon)
    
    print(len(data))
    
    return JsonResponse({})