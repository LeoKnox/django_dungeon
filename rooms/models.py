from django.db import models

class Room(models.model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    width = models.IntegerField()
    length = models.IntegerField()