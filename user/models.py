from django.db import models


# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(("email address"), blank=True,unique=True)
    gender=models.CharField(max_length=10)
    age=models.IntegerField(max_length=2)
    img = models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    dog_id=models.IntegerField()
    bio = models.TextField()

    def __str__(self):  #admin panelinde kullanıcılar kaydettiğimizde isimleri görünecek.
        return self.first_name


    
    