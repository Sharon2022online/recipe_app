# Generated by Django 4.1.5 on 2023-04-09 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='publish',
        ),
    ]