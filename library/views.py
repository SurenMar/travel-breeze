from django.shortcuts import render

# Import models
from library.models import Destination, MonthlyWeather

def destination_list(request):
    destinations = Destination.objects.order_by('date_added')
    context = {
        'title': 'Library', 
        'destinations': destinations,
    }
    return render(request, 'library/destination_list.html', context)


def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    weather_data = destination.monthly_stats.order_by('month')
    context = {
        'title': 'city name',
        'weather_data': weather_data,
    }
    return render(request, 'library/destination_detail.html', context)
