from django.urls import path

from . import views

app_name = 'explore'
urlpatterns = [
    # World map page
    path('', views.world_map, name='world_map'),
    
    # Call APIs with coord data
    path('save-data/', views.save_data, name='save_data'),
]

