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
    
    # Initialize variables for graph
    data, y_bounds = [], []
    title, y_label = '', ''
    weather_data = destination.monthly_stats.order_by('month')
     
    if 'humidity' in request.GET:
        data = [wd.humidity for wd in weather_data]
        title = 'Average Monthly Humidity'
        y_label = 'Humidity'
        y_bounds = [0, 100]
        
    elif 'prcp' in request.GET:
        data = [wd.precipitation for wd in weather_data]
        title = 'Average Monthly Precipitation'
        y_label = 'Precipitation'
        y_bounds = [0, 500]
        
    elif 'wdsp' in request.GET:
        data = [wd.wind_speed for wd in weather_data]
        title = 'Average Monthly Wind Speed'
        y_label = 'Wind Speed'
        y_bounds = [0, 25]
        
    else:
        data = [wd.avg_temp for wd in weather_data]
        data = [wd.avg_temp for wd in weather_data]
        title = 'Average Monthly Temprature'
        y_label = 'Temprature'
        y_bounds = [-50, 50]
    
    fig = px.bar(
        x=[i+1 for i in range(12)],
        y=data,
        labels={'x': 'Months', 'y': y_label},
        title=title,
        range_y=y_bounds,
    )
    chart = fig.to_html()
    context = {
        'title': 'city name',
        'weather_data': weather_data,
        'chart': chart,
        'destination': destination
    }
    return render(request, 'library/destination_detail.html', context)
