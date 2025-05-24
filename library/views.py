from django.shortcuts import render


def destination_list(request):
    context = {'title': 'Library'}
    return render(request, 'library/destination_list.html', context)


def destination_detail(request):
    context = {'title': 'city name'}
    return render(request, 'library/destination_detail.html', context)
