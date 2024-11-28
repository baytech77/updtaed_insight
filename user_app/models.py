from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES =(('M', 'Male'),
                 ('F', 'Female')
                 )


class CustomUser(AbstractUser):
    # Your custom fields go here

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this to avoid conflict
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    age = models.SlugField( null=True)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255)
    phone_number = models.SlugField( null=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=6)
