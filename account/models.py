from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, unique =True, null=True)
    email = models.EmailField(unique=True, null=True)
    country = models.CharField(max_length=40, null=True)

    photo = models.ImageField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []