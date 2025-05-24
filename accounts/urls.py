from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    # Login page
    path('', views.login, name='login'),
    
    # Registration page
    path('register/', views.register, name='register'),
]
