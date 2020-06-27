from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class WareHouse(models.Model):
    name     = models.CharField(max_length=40,blank=False) 
    lat      = models.CharField(max_length=10,blank=False)
    lng      = models.CharField(max_length=10,blank=False)
    capacity = models.FloatField(blank=False)
    filled   = models.FloatField(blank=False)
    left     = models.FloatField(blank=True)
    hascs    = models.BooleanField(blank=False,default=False,verbose_name="Has Cold Store")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    def info(self):
        msg = "<h3>Name : {}</h3><br> Full capacity : {} kg<br> Filled Capacity : {} kg<br> LeftOver Capacity : {} kg <br> Cold Store".format(self.name,self.capacity,self.filled,self.left)
        if self.hascs:
            msg=msg+"   &#10004;"
        else:
            msg=msg+"	&#10060;"

        return msg

@receiver(pre_save,sender=WareHouse)
def writeleft(sender=WareHouse,instance=None,created=False,**kwargs):
    #updating left field
    if not instance.left:
        instance.left=float(instance.capacity-instance.filled)
    