from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Observation(models.Model):
    species = models.CharField(max_length=250, blank=True)
    appearance = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='time')
    place = models.CharField(max_length=250)
    time = models.DateTimeField(default=timezone.now)
    number = models.IntegerField()
    description = models.TextField(blank=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observations')

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse('birdnotes:observation_detail',
                       args=[self.time.year,
                             self.time.strftime('%m'),
                             self.time.strftime('%d'),
                             self.slug
                             ])

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.species), slugify(self.place)))
        super(Observation, self).save(*args, **kwargs)


class BirdSpecies(models.Model):
    latin_name = models.CharField(max_length=250)
    polish_name = models.CharField(max_length=250)
    category = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ('polish_name',)

    def __str__(self):
        return self.polish_name
