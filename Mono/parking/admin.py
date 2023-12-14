from django.contrib import admin

# Register your models here.
from . import models


class CarAdmin(admin.ModelAdmin):
    list_display = ["brand_car", "state_number", "client", ]


class CarClient(admin.ModelAdmin):
    list_display = ["name", ]


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Client, CarClient)
