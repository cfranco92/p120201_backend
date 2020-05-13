# Generated by Django 3.0.4 on 2020-05-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasonic', '0002_ultrasonic_placelatitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='ultrasonic',
            name='placeLength',
            field=models.IntegerField(default=3452, verbose_name='PlaceLength'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ultrasonic',
            name='terrainArea',
            field=models.IntegerField(default=6575, verbose_name='TerrainArea'),
            preserve_default=False,
        ),
    ]
