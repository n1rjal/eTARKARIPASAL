from django.contrib import admin
from .models import Items,Complain,Transaction

# Register your models here.
admin.site.register(Items)
admin.site.register(Complain)
admin.site.register(Transaction)