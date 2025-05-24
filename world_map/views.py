from django.shortcuts import render, redirect

def world_map(request):
    return render(request, 'world_map/world_map.html')
