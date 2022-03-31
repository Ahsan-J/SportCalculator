from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.CharField(max_length=125, primary_key=True, unique=True)
    name = models.CharField(max_length=264, unique=True)
    location = models.CharField(max_length=264)
    email = models.CharField(max_length = 264)

    def __str__(self):
        return self.name