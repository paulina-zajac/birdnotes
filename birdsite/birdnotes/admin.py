from django.contrib import admin
from .models import Observation, BirdSpecies

# Register your models here.
@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('species','time','place', 'person',)
    list_filter = ('time', 'person')
    prepopulated_fields = {'slug': ('species','place')}
    raw_id_fields = ('person',)
    date_hierarchy = 'time'
    ordering = ('time',)

@admin.register(BirdSpecies)
class BirdSpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'latin_name', 'polish_name', 'category', 'state')
    list_filter = ('category',)
    ordering = ('polish_name',)
