# Generated by Django 4.1.7 on 2023-02-21 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='r_desc',
            field=models.CharField(max_length=2550),
        ),
        migrations.CreateModel(
            name='ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=55)),
                ('unit', models.CharField(max_length=80)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_app.recipe')),
            ],
        ),
    ]