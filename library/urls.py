from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    # List of all destinations saved
    path('', views.destination_list, name='destination_list'),
    
    # Show selected destination
    path('destination/', views.destination_detail, name='destination_detail'),
    
    # Call APIs with coord data
    path('save-data/', views.save_data, name='save_data'),
]
