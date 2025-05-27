from django.shortcuts import render
from django.http import JsonResponse


def destination_list(request):
    context = {'title': 'Library'}
    return render(request, 'library/destination_list.html', context)


def destination_detail(request):
    context = {'title': 'city name'}
    return render(request, 'library/destination_detail.html', context)

def save_data(request):
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')
    print(lat, lon)
    return JsonResponse({})

    # pass data to weather_api to get info
    # also install geopy
