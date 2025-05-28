"""
A file to request API calls for country data
"""

from geopy.geocoders import Nominatim

# Initialize geocoder
geolocator = Nominatim(user_agent="travel_breeze_country_api")

def get_country_data(lat, lon):
    """
    A function to return country and city name based on coordinate values
    """
    # Perform reverse geocoding
    location = geolocator.reverse((lat, lon), language='en')

    # Extract city and country, return None if error is encountered
    if location and location.raw.get('address'):
        address = location.raw['address']
        city = address.get('city', address.get('town', address.get('village')))
        country = address.get('country')
        return country, city
    else:
        return None, None
