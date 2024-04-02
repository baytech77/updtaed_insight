from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES =(('M', 'Male'),
                 ('F', 'Female')
                 )


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(unique=True)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255)
    phone_number = models.SlugField( unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='Male')
