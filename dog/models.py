from django.db import models
import uuid


class Dog(models.Model):
    #id=models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    # img=models.ImageField(null=True,blank=True)
    age = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=500)


    def __str__(self):  #admin panelinde köpkeleri kaydettiğimizde isimleri görünecek.
        return self.name



