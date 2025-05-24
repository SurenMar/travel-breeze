"""
URL configuration for weather_vista project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin site
    path('admin/', admin.site.urls),
    
    # Home page
    path('', include('core.urls')),
    
    # User accounts (sign in, sign up)
    path('accounts/', include('accounts.urls')),
    
    # World map page
    path('world-map/', include('world_map.urls')),
    
    # List of all saved destinations
    path('library/', include('library.urls')),
]
