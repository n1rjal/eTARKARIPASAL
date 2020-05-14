from django.contrib import admin
from .models import Job,ProfilePicture,GeoData

# Register your models here.
admin.site.register(Job)
admin.site.register(ProfilePicture)
admin.site.register(GeoData)