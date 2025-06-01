# Import Django
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

# Import other tools
import json

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
    # Get latitude and longitude from user's clicks
    user_click = json.loads(request.body)
    destinations = user_click.get('destinations', [])
    
    # List of all the destinations which dont give enough data
    invalid_dests = []

    for dest in destinations:
        # Debugging
        print('---------------------------------------------------------------------')
        lat = dest.get('latitude')
        lon = dest.get('longitude')
    
        # Get country and city name through API (no need to parse)
        country, city = get_country_data(lat, lon)
        
        # Get weather data through API call and parse it
        raw_weather_data = get_weather_data(lat, lon)
        parsed_weather_data = parse_weather_data(raw_weather_data)
        # Check if parsing failed (no weather stations with needed data)
        if len(parsed_weather_data) == 0:
            invalid_dests.append(dest)
        # Analyze data
        else:
            weather_data = monthly_weather_avgs(parsed_weather_data)
        
            # Save data to database
            destination_pk = save_destination(request.user, country, city, lat, lon)
            save_monthly_weather(destination_pk, weather_data)
            
            print(len(weather_data))
            print(country)
            print(city)
    
    # Return to frontend all invalid destinations
    return JsonResponse({
        'invalid_dests': invalid_dests
    }, status=200)