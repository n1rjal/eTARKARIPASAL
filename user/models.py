from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):

    choices=(
        ("TP","ShopKeeper"),
        ("TK","Normal User"),
        ("TB","Farmer"),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    job=models.CharField(max_length=2,choices=choices,default='TK')
    
    def __str__(self):
        return str(self.user)+" => "+str(self.job)

#current location must be dynamic 
class GeoData(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    choices=(("MALE","MALE"),
            ("FEMALE","FEMALE"),
            ("LET'S NOT SAY ","LETS NOT SAY"))
    sex=models.CharField(max_length=14,choices=choices,default="MALE")
    about=models.TextField(verbose_name=u"Bio")
    address=models.CharField(max_length=100,null=True)
    phone1=models.CharField(verbose_name=u"Phone Number [empty if you don't want to show it]",blank=True,max_length=13,null=True)
    
    def __str__(self):
        return self.user.username