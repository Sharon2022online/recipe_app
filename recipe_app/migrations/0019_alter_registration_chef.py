# Generated by Django 4.1.5 on 2023-03-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0018_alter_registration_chef'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='chef',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3),
        ),
    ]