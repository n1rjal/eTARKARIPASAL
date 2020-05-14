from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

class ProfilePicture(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pp=models.ImageField(upload_to="pp",blank=False)

    def save(self):
        super().save()
        size=(300,300)
        
        print(self.pp.url)
        photo=Image.open(self.pp.path)
        if photo.height>300 or photo.width>300:
            photo.thumbnail(size)
            photo.save(self.pp.path)
    
    def __str__(self):
        return self.user.username

#current location must be dynamic 
class GeoData(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    about=models.TextField(verbose_name=u"Bio")
    address=models.CharField(max_length=100,null=True)
    phone1=models.CharField(verbose_name=u"Phone Number [empty if you don't want to show it]",max_length=13,null=True)
    
    def __str__(self):
        return self.user.username