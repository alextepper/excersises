from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75, unique=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name
