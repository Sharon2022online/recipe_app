# Generated by Django 4.1.5 on 2023-04-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=255)),
                ('recipe_image', models.ImageField(default='food.png', upload_to='recipes/')),
                ('prep_time', models.PositiveIntegerField(default='NIL')),
                ('serves', models.PositiveIntegerField(default=0)),
                ('type', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], max_length=7)),
                ('ingredient', models.TextField(default='NIL')),
                ('description', models.TextField(default='NIL')),
                ('publish', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('chef', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3)),
                ('pic', models.ImageField(default='profile.png', upload_to='profile_pics/')),
            ],
        ),
    ]
