from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Import models
from .models import Destination, MonthlyWeather

# Import Plotly
import plotly.express as px

@login_required
def destination_list(request):
    destinations = Destination.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'title': 'Library', 
        'destinations': destinations,
    }
    return render(request, 'library/destination_list.html', context)


@login_required
def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    
    # Verify destination belongs to current user
    if destination.owner != request.user:
        raise Http404
    
    data = []
    weather_data = destination.monthly_stats.order_by('month')
    if request.method == 'POST':
        if 'temp' in request.POST:
            data = [wd.avg_temp for wd in weather_data]
        elif 'humidity' in request.POST:
            data = [wd.humidity for wd in weather_data]
        elif 'prcp' in request.POST:
            data = [wd.precipitation for wd in weather_data]
        elif 'wdsp' in request.POST:
            data = [wd.wind_speed for wd in weather_data]
    else:
        data = [wd.avg_temp for wd in weather_data]
    
    fig = px.bar(
        x=[i+1 for i in range(12)],
        y=data,
    )
    chart = fig.to_html()
    context = {
        'title': 'city name',
        'weather_data': weather_data,
        'chart': chart,
        'destination': destination
    }
    return render(request, 'library/destination_detail.html', context)
