from django.shortcuts import render, redirect

def world_map(request):
    return render(request, 'explore/world_map.html')
