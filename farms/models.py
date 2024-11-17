from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Farm(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.FloatField()

    def __str__(self):
        return self.name


class Crop(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    planting_date = models.DateField()
    harvest_date = models.DateField()

    def __str__(self):
        return self.name


class Animal(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
