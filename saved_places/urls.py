from django.urls import path

from . import views

app_name = 'saved_places'
urlpatterns = [
    # List of all destinations saved
    path('', views.all_destinations, name='all_destinations'),
    
    # Show selected destination
    path('destination/', views.destination, name='destination'),
]
