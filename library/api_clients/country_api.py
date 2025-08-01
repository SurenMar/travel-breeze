"""
A file to request API calls for country data
"""
# Import Geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import ssl
import certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Import time
from time import sleep

# Initialize geocoder
geolocator = Nominatim(user_agent='travel_breeze_country_api')

def get_country_data(lat, lon):
    """
    A function to return country and city name based on coordinate values
    """
    # Perform reverse geocoding with delay
    MAX_ATTEMPTS = 5
    for _ in range(MAX_ATTEMPTS):
        try:
            location = geolocator.reverse((lat, lon), language='en')
        except GeocoderTimedOut:
            sleep(1)

    # Extract city and country name
    if location and location.raw.get('address'):
        address = location.raw['address']
        country = address.get('country')
        country = country.title() if country else 'the ocean'
        city = address.get('city', address.get('town', address.get('village')))
        city = city.title() if city else 'Somewhere in'
        return country, city
    else:
        return 'the ocean', 'Somewhere in'


def get_coord_data(city, country):
    """
    A function to return coords of country and city
    """
    # Double check that neither input is an empty string
    if not city or not country:
        return None
    # Perform geocoding with delay
    MAX_ATTEMPTS = 5
    for _ in range(MAX_ATTEMPTS):
        try:
            coords = geolocator.geocode(f'{city}, {country}')
        except GeocoderTimedOut:
            sleep(1)
    if coords:
        return {'latitude': coords.latitude, 'longitude': coords.longitude}
    