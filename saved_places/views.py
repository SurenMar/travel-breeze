from django.shortcuts import render


def all_destinations(request):
    return render(request, 'saved_places/all_destinations.html')


def destination(request):
    return render(request, 'saved_places/destination.html')
