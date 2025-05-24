from django.shortcuts import render


def index(request):
    context = {'title': 'home'}
    return render(request, 'core/index.html', context)