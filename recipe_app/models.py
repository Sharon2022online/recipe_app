from django.db import models
from django import forms

# Create your models here.
class login(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class registration(models.Model):
    CHEF_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    chef = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='profile_pics/',default='profile.png')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_image = models.ImageField(upload_to='recipes/',default='food.png')
    prep_time = models.PositiveIntegerField(default='NIL')
    serves = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=7, choices=(('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')))
    ingredient=models.TextField(default='NIL')
    description = models.TextField(default='NIL')
    publish = models.ForeignKey(registration, on_delete=models.CASCADE)
    def __str__(self):
        return self.recipe_name
   
    


