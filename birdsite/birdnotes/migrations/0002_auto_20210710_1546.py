# Generated by Django 3.2.5 on 2021-07-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdnotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='observation',
            name='species',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]