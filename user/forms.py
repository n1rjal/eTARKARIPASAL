from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django import forms as Fform

from.models import Job,ProfilePicture,GeoData


class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

class UserJobForm(Fform.ModelForm):
    class Meta:
        model=Job

        fields=[
            'job'
        ]
    
class GeodataForm(Fform.ModelForm):
    class Meta:
        model=GeoData
        fields=[
            'phone1',
            'address',
            'about'
        ]


class UserLoginForm(forms.AuthenticationForm):
    model=User

    fields=[
        "username",
        "email",
        "password"
    ]

class ProfilePictureForm(Fform.ModelForm):
    class Meta:
        model=ProfilePicture

        fields=[
            "pp",
        ]