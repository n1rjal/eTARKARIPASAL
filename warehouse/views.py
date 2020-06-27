from django.shortcuts import render
from django.views import View
from . import models

from user.models import User
from items.models import Items
# Create your views here.
    
class Home(View):
    #site's home
    def get(self,request):
        allusers = User.objects.all()
        whs      = models.WareHouse.objects.all()
        allitems = Items.objects.all()
        return render(request,"warehouse/maps.html",{"whs":whs,"allitems":allitems,"allusers":allusers})