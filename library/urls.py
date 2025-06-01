from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    # List of all destinations saved
    path('', views.destination_list, name='destination_list'),
    
    # Show selected destination
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    
    # Show month for selected destination
    path('destination/<int:destination_id>/<int:month>', views.destination_month, name='destination_month'),
]
