from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Items(models.Model):
    
    name=models.CharField(max_length=100,blank=False)
    image=models.ImageField(default="items/vege.jpg",upload_to="items")
    #r -> Retail
    #w -> Wholesale

    rprice=models.IntegerField()
    wprice=models.IntegerField()
    
    def __str__(self):
        return self.name

    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            img.thumbnail((300,300))
            img.save(self.image.path)


    def getjson(self):
        return ({
            "name":self.name,
            "wprice":self.wprice,
            "rprice":self.rprice
        })


class Complain(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    text=models.TextField(verbose_name=u"Feedback",blank=True,null=True)
    rate=models.FloatField(verbose_name=u"Rate my work out of 10",validators=[MinValueValidator(1.0),MaxValueValidator(10.0)])
    date=models.DateField(auto_now=True)
    def __str__(self):
        return ("{} - {}/10".format(self.user.username,self.rate))

class Transaction(models.Model):
    datetime=models.DateTimeField(auto_now=True)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    transactiontext=models.TextField()
    

    def __str__(self):
        return self.user.paidamount