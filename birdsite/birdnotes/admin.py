from django.contrib import admin
from .models import Observation

# Register your models here.
@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('id','species', 'time','place', 'person',)
    list_filter = ('time', 'person')
    prepopulated_fields = {'slug': ('species','place')}
    raw_id_fields = ('person',)
    date_hierarchy = 'time'
    ordering = ('time',)
