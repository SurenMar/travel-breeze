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
from library.utils.processors import process_weather_avgs
from library.utils.processors import clean_weather_data

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


def _destination_exists(user, country, city):
    """
    A helper function that checks if a destination already exists
    """
    if city != 'Somewhere in' and Destination.objects.filter(
       owner=user, country=country, city=city).exists():
        return True
    else:
        return False


def _process_weather_data(destinations, user):
    """
    A helper function that cleans, processes, and saves data in database.
    Returns any invalid destinations.
    """
    invalid_dests = []
    # Check each of the users clicked destinations
    for dest in destinations:
        # Get lat and lon values of dest
        lat = dest.get('latitude')
        lon = dest.get('longitude')
    
        # Get country and city name through API (no need to parse)
        # Dont add to db if it already exists
        country, city = get_country_data(lat, lon)
        print(country, city)
        if _destination_exists(user, country, city):
            continue
        
        # Get weather data through API call and clean it
        raw_weather_df = get_weather_data(lat, lon)
        clean_weather_df = clean_weather_data(raw_weather_df)
        # Check if cleaning failed (no weather stations with needed data)
        print('------------')
        print(len(clean_weather_df))
        print('------------')
        if len(clean_weather_df) == 0:
            invalid_dests.append(dest)
        # Analyze data
        else:
            monthly_weather = process_weather_avgs(clean_weather_df)
            # Save data to database
            destination_pk = save_destination(user, country, city, lat, lon)
            save_monthly_weather(destination_pk, monthly_weather)
        
    return invalid_dests

@login_required
def save_data(request):
    """
    A view which recieves/sends/processes requests regarding weather/map data
    """
    if 'enter_location' in request.POST:
        print('ENTER LOCATION')
        country_form = CountryForm(data=request.POST)
        city_form = CityForm(data=request.POST)
        
        if country_form.is_valid() and city_form.is_valid():
            country = country_form.cleaned_data['country'].title()
            city = city_form.cleaned_data['city'].title()
            # Check if location already exists in datab
            if _destination_exists(request.user, country, city) and city != 'Somewhere In':
                return JsonResponse({
                    'duplicate_error': True,
                }, status=200)
            
            coords = get_coord_data(city, country)
            # Check if location could not be found, return location error
            if not coords:
                return JsonResponse({
                    'location_error': True,
                }, status=200)
            # Return coords
            else:
                lat, lon = coords['latitude'], coords['longitude']
                return JsonResponse({
                    'lat': lat,
                    'lon': lon,
                }, status=200)
            
    # Get latitude and longitude from user's clicks
    user_click = json.loads(request.body)
    destinations = user_click.get('destinations', [])
    print('PROCESSING CLICKS')
    print(destinations)
    
    # Process weather data
    invalid_dests = _process_weather_data(destinations, request.user)
    print(invalid_dests)
    
    # Return all invalid destinations to frontend
    return JsonResponse({
        'invalid_dests': invalid_dests
    }, status=200)