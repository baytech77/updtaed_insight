# Generated by Django 4.2.6 on 2023-12-25 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_courses_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='author',
        ),
    ]
