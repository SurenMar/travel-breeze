# Import Django
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Import models and forms
from library.models import Destination
from library.forms import CountryForm, CityForm

# Import api clients
from library.api_clients.weather_api import get_weather_data
from library.api_clients.country_api import get_country_data, get_coord_data

# Import utils
from library.utils.parsers import parse_weather_data
from library.utils.analysis import monthly_weather_avgs

# Import services
from library.services.save_to_db import save_destination, save_monthly_weather

# Import other tools
import json

@login_required
def world_map(request):
    """
    A view that displays map
    """
    # Get the coordinates of all destination of current user
    destinations = list(Destination.objects.filter(owner=request.user) \
        .values('latitude', 'longitude'))
    # Create empty city and country forms
    country_form = CountryForm()
    city_form = CityForm()
    context = {
        'title': 'Explore',
        'destinations': destinations,
        'country_form': country_form,
        'city_form': city_form,
    }
    return render(request, 'explore/world_map.html', context)


def _process_weather_data(destinations, user):
    """
    A helper function that analyzes, parses, and saves data in database.
    Returns any invalid destinations.
    """
    invalid_dests = []      # A list of all invalid destinations
    # Check each of the users clicked destinations
    for dest in destinations:
        # Get lat and lon values of dest
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
            destination_pk = save_destination(user, country, city, lat, lon)
            save_monthly_weather(destination_pk, weather_data)
        
    return invalid_dests

@login_required
def save_data(request):
    """
    A view which recieves/sends/processes requests regarding weather/map data
    """
    if 'enter_location' in request.POST:
        country_form = CountryForm(data=request.POST)
        city_form = CityForm(data=request.POST)
        
        if country_form.is_valid() and city_form.is_valid():
            country = country_form.cleaned_data['country']
            city = city_form.cleaned_data['city']
            
            coords = get_coord_data(city, country)
            lat, lon = coords['latitude'], coords['longitude']
            if not lat or not lon:
                return JsonResponse({
                    'location_error': True,
                }, status=400)
            else:
                return JsonResponse({
                    'lat': lat,
                    'lon': lon,
                }, status=200)
            
    # Get latitude and longitude from user's clicks
    user_click = json.loads(request.body)
    destinations = user_click.get('destinations', [])
    
    # Process weather data
    invalid_dests = _process_weather_data(destinations, request.user)
    
    # Return all invalid destinations to frontend
    return JsonResponse({
        'invalid_dests': invalid_dests
    }, status=200)