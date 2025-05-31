from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

# Import models
from library.models import Destination

# Import api clients
from library.api_clients.weather_api import get_weather_data
from library.api_clients.country_api import get_country_data

# Import utils
from library.utils.parsers import parse_weather_data
from library.utils.analysis import monthly_weather_avgs

# Import services
from library.services.save_to_db import save_destination, save_monthly_weather

@login_required
def world_map(request):
    # Get the coordinates of all destination of current user
    destinations = list(Destination.objects.filter(owner=request.user) \
        .values('latitude', 'longitude'))
    context = {
        'title': 'Explore',
        'destinations': destinations,
    }
    return render(request, 'explore/world_map.html', context)


@login_required
def save_data(request):
    """
    A view which gets data, parses it, and stores in database
    """
    # Get latitude and longitude from user click
    data = json.loads(request.body)
    destinations = data.get('destinations', [])

    # Example: just print them (replace with your save logic)
    for dest in destinations:
        print('---------------------------------------------------------------------')
        lat = dest.get('latitude')
        lon = dest.get('longitude')
    
        # Get country and city name through API (no need to parse)
        country, city = get_country_data(lat, lon)
        
        # Get weather data through API call, parse it and analyze it
        raw_data = get_weather_data(lat, lon)
        parsed_data = parse_weather_data(raw_data)
        data = monthly_weather_avgs(parsed_data)
        
        # for debugging
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        # Save data to database
        destination_pk = save_destination(request.user, country, city, lat, lon)
        save_monthly_weather(destination_pk, data)
        
        print(len(data))
        print(country)
        print(city)
    
    return JsonResponse({})