from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Login page
    path('', include('django.contrib.auth.urls')),
    
    # Registration page
    path('register/', views.register, name='register'),
]
