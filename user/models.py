from django.db import models
import uuid

# Create your models here.


def generate_upload_path(instance, filename):
    return f'profile_photos/{instance.id}/{filename}'


class User(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(("email address"), blank=True,unique=True)
    gender=models.CharField(max_length=10)
    age=models.IntegerField(max_length=2)
    image=models.ImageField(null=True,blank=True,upload_to=generate_upload_path)
    city=models.CharField(max_length=100)
    password = models.CharField(length=10)
    dog_id=models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    bio = models.TextField()

    # to save the data
    def register(self): 
        self.save()


    