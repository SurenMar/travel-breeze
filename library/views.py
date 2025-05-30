from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Import models
from .models import Destination

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
    
    weather_data = destination.monthly_stats.order_by('month')
    context = {
        'title': 'city name',
        'weather_data': weather_data,
    }
    return render(request, 'library/destination_detail.html', context)
