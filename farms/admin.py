from django.contrib import admin

# Register your models here.

from .models import Farm, Crop, Animal


class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'size', 'owner')
    list_filter = ('location', 'owner')


class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'planting_date', 'harvest_date', 'farm')
    list_filter = ('type', 'planting_date', 'harvest_date', 'farm')


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'birth_date', 'farm')
    list_filter = ('species', 'birth_date', 'farm')


admin.site.register(Farm, FarmAdmin)
admin.site.register(Crop, CropAdmin)
admin.site.register(Animal, AnimalAdmin)
