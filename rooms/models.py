from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    floor_texture = models.ImageField(upload_to='images/')
    width = models.IntegerField()
    length = models.IntegerField()