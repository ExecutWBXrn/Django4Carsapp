# Generated by Django 5.0 on 2024-01-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsmaincategory', '0007_tagpost_cars_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'DRAFT'), (1, 'PUBLISHED')], default=1),
        ),
    ]