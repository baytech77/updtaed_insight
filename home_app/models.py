from django.db import models
from django.utils import timezone
from datetime import date


# defining default language


def default_language():
    return f"English"
# Create your models here.


class Courses(models.Model):

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=225)
    updated = models.DateField(default=date.today)
    language = models.CharField(max_length=30, default=default_language)
    noOfStudent = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/courses')

    def __str__(self):
        return f"{self.title[:50]}"
        # created_by:{self.created_by},updated:{self.updated},date_created:{self.date_created}"
