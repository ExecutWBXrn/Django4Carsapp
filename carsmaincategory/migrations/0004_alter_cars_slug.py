# Generated by Django 5.0 on 2024-01-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsmaincategory', '0003_alter_cars_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]