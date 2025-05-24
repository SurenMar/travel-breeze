from django.urls import path

from . import views

app_name = 'explore'
urlpatterns = [
    # World map page
    path('', views.world_map, name='world_map'),
]

