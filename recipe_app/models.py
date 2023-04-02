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
    chef = models.CharField(max_length=3, choices=CHEF_CHOICES)
    pic = models.ImageField(upload_to='profile_pics/',default='profile.png')


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_image = models.ImageField(upload_to='recipes/',default='food.png')
    prep_time = models.PositiveIntegerField(default='NIL')
    serves = models.PositiveIntegerField(default=0)
    veg = models.BooleanField(default=0)
    non_veg = models.BooleanField(default=0)
    dessert= models.BooleanField(default=0)
    description = models.TextField(default='NIL')
    


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    i_name = models.CharField(max_length=255)
    qty = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50)


