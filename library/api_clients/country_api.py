"""
A file to request API calls for country data
"""
# Import Geopy
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Import time
from time import sleep

# Initialize geocoder
geolocator = Nominatim(user_agent="travel_breeze_country_api")

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

    # Extract city and country, return None if error is encountered
    if location and location.raw.get('address'):
        address = location.raw['address']
        country = address.get('country')
        city = address.get('city', address.get('town', address.get('village'))) \
            or 'A city in'
        return country, city
    else:
        return None, None
