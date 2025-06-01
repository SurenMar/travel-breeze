from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Import models
from .models import Destination, MonthlyWeather

# Import Plotly
import plotly.express as px

# Global constants
MONTHS = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
]

@login_required
def destination_list(request):
    destinations = Destination.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'title': 'Library', 
        'destinations': destinations,
    }
    return render(request, 'library/destination_list.html', context)


def _graph_info(buttons_clicked, weather_data):
    """
    A helper function to pick out appropriate attributes for the bar graph
    """
    
    # Check if user wants to see humidity data
    if 'humidity' in buttons_clicked:
        data = [wd.humidity for wd in weather_data]
        title = 'Average Monthly Humidity'
        y_label = 'Humidity'
        suffix = '%'
    
    # Check if user wants to see precipitation data
    elif 'prcp' in buttons_clicked:
        data = [wd.precipitation for wd in weather_data]
        title = 'Average Monthly Precipitation'
        y_label = 'Precipitation'
        suffix = ' mm'
    
    # Check if user wants to see wind speed data
    elif 'wdsp' in buttons_clicked:
        data = [wd.wind_speed for wd in weather_data]
        title = 'Average Monthly Wind Speed'
        y_label = 'Wind Speed'
        suffix = ' km/h'
    
    # Check if user wants to see tempreature data or just loaded into the page
    else:
        data = [wd.avg_temp for wd in weather_data]
        title = 'Average Monthly Temprature'
        y_label = 'Temprature'
        suffix = ' °C'
        
    return {
        'data': data,
        'title': title,
        'y_label': y_label,
        'suffix': suffix,
    }


@login_required
def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    
    # Verify destination belongs to current user
    if destination.owner != request.user:
        raise Http404
    
    # Get weather data for desired destination
    weather_data = destination.monthly_stats.order_by('month')
    
    graph_info = _graph_info(request.GET, weather_data)
    
    # Create plotly bar graph
    y_bounds = [min(0, min(graph_info['data'])) * 1.3, 
                max(graph_info['data']) * 1.3]
    fig = px.bar(
        x=MONTHS,
        y=graph_info['data'],
        labels={'x': 'Months', 'y': graph_info['y_label']},
        title=graph_info['title'],
        range_y=y_bounds,
    )
    fig.update_layout(
        yaxis=dict(
            ticksuffix=graph_info['suffix']
        )
    )
    
    chart = fig.to_html()
    context = {
        'title': 'detailed forecast',
        'weather_data': weather_data,
        'chart': chart,
        'destination': destination
    }
    return render(request, 'library/destination_detail.html', context)


@login_required
def destination_month(request, destination_id, month):
    destination = Destination.objects.get(id=destination_id)
    
    if destination.owner != request.user:
        raise Http404
    
    month_data = destination.monthly_stats.get(month=month)
    
    context = {
        'title': 'detailed forecast',
        'month': MONTHS[month-1],
        'month_data': month_data,
        'destination': destination,
    }
    return render(request, 'library/destination_month.html', context)
