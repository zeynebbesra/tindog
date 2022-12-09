from django.db import models
import uuid
# Create your models here.


def generate_upload_path(instance, filename):
    return f'profile_photos/{instance.id}/{filename}'

class Dog(models.Model):
    #dog_id=models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name=models.CharField(max_length=30)
    breed=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    img=models.ImageField(null=True,blank=True,upload_to=generate_upload_path)
    age = models.IntegerField(blank=True, null=True)


    # to save the data
    def register(self): 
        self.save()



