from django.shortcuts import render


def saved_destinations(request):
    context = {'title': 'Library'}
    return render(request, 'library/saved_destinations.html', context)


def destination(request):
    context = {'title': 'city name'}
    return render(request, 'library/destination.html', context)
