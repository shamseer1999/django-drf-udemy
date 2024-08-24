# Generated by Django 5.1 on 2024-08-24 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_riview_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riview',
            name='rating',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
