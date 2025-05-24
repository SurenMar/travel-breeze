from django.shortcuts import render


def login(request):
    context = {'title': 'Login'}
    return render(request, 'accounts/login.html', context)


def register(request):
    context = {'title': 'Register'}
    return render(request, 'accounts/register.html', context)
