from django.db import models

# Create your models here.
class Report(models.Model):
    WEATHER_CHOICES = [
        ('sunny', 'Sunny'),
        ('cloudy', 'Cloudy'),
        ('windy', 'Windy'),
        ('rainy', 'Rainy'),
        ('stormy', 'Stormy'),
    ]

    location = models.CharField(max_length=255)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=6, choices=WEATHER_CHOICES, default='sunny')

    def __str__(self):
        return self.location