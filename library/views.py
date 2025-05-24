from django.shortcuts import render


def saved_destinations(request):
    return render(request, 'library/saved_destinations.html')


def destination(request):
    return render(request, 'library/destination.html')
