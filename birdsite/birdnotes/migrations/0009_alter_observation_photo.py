# Generated by Django 3.2.5 on 2021-07-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdnotes', '0008_observation_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]