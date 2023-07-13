from django.db import models


class Room(models.Model):
    number = models.CharField(max_length=20)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    objects = models.Manager()
