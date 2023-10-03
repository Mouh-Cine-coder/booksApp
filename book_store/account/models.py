from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Customer(AbstractUser):
    user_image =  models.ImageField(upload_to ='imagesUsers/', blank=True, null=True)

