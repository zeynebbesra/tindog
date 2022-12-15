from django.db import models
import uuid


class Dog(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    age = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=500)


    def __str__(self):  #admin panelinde köpkeleri kaydettiğimizde isimleri görünecek.
        return self.name



