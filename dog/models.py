from django.db import models

class Dog(models.Model):
    #id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    age = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=500)


    def __str__(self):  #admin panelinde köpkeleri kaydettiğimizde isimleri görünecek.
        return self.name

class User(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, blank=True)
    #id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(("email address"), blank=True,unique=True)
    age=models.IntegerField(max_length=2)
    city=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    #dog_id=models.IntegerField()
    img = models.CharField(max_length=500)
    bio = models.TextField()
    

    def _str_(self):  #admin panelinde kullanıcılar kaydettiğimizde isimleri görünecek.
        return self.first_name





