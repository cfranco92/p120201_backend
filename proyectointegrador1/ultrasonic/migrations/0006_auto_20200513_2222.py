# Generated by Django 3.0.4 on 2020-05-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasonic', '0005_auto_20200513_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ultrasonic',
            name='terrainArea',
        ),
        migrations.AddField(
            model_name='ultrasonic',
            name='landArea',
            field=models.TextField(default=1, verbose_name='LandArea'),
            preserve_default=False,
        ),
    ]
