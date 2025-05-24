from django.shortcuts import render, redirect

def world_map(request):
    context = {'title': 'Explore'}
    return render(request, 'explore/world_map.html', context)
