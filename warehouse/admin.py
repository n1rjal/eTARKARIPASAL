from django.contrib import admin
from . import models
# Register your models here.

class WarehouseClass(admin.ModelAdmin):
    list_display=("name","capacity","filled","left")

admin.site.register(models.WareHouse)