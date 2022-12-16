from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(("email address"), blank=True,unique=True)
    age=models.IntegerField(max_length=2)
    city=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    dog_id=models.IntegerField()
    img = models.CharField(max_length=500)
    bio = models.TextField()

    def _str_(self):  #admin panelinde kullanıcılar kaydettiğimizde isimleri görünecek.
        return self.first_name







