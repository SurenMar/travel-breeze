from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    # List of all destinations saved
    path('', views.saved_destinations, name='saved_destinations'),
    
    # Show selected destination
    path('destination/', views.destination, name='destination'),
]
