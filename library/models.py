from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):
    """
    A destination the user saved
    """
    # Basic information
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # Country information
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    # Location information
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.country}, {self.city}"
    

class MonthlyWeather(models.Model):
    """
    A months weather data for a specific destination
    """
    # Create tuples for each month
    MONTH_CHOICES = [(i, month) for i, month in enumerate([
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ], start=1)]
    
    # Basic information
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='monthly_stats')
    month = models.IntegerField(choices=MONTH_CHOICES)
    
    # Temprature information
    avg_temp = models.FloatField(null=True)
    max_temp = models.FloatField(null=True)
    min_temp = models.FloatField(null=True)
    # Humidity information
    humidity = models.FloatField(null=True)
    # Percipitation information
    precipitation = models.IntegerField(null=True)
    # Wind information
    wind_speed = models.FloatField(null=True)
    # Other
    weather_code = models.IntegerField(null=True)
    
    class Meta:
        ordering = ['month']
        constraints = [
            models.UniqueConstraint(fields=['destination', 'month'], name='unique_destination_month')
        ]
        
    def __str__(self):
        display = f"\n{self.month}: {self.avg_temp}, {self.wind_speed}\n"
        print('here')
        return display

        


