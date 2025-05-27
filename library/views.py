from django.shortcuts import render
from django.http import JsonResponse

from library.api_clients.weather_api import get_weather_data
from library.api_clients.country_api import get_country_data


def destination_list(request):
    context = {'title': 'Library'}
    return render(request, 'library/destination_list.html', context)


def destination_detail(request):
    context = {'title': 'city name'}
    return render(request, 'library/destination_detail.html', context)

def save_data(request):
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')
    data = get_weather_data(lat, lon)
    country, city = get_country_data()
    
    return JsonResponse({})

    # pass data to weather_api to get info
    # also install geopy
