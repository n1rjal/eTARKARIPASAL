from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django import forms as Fform

from.models import Job,GeoData


class UserRegisterForm(UserCreationForm):
    password1 = Fform.CharField(
    help_text='Enter Password', required=True,
    widget=Fform.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
    )

    password2 = Fform.CharField(
        help_text='Enter Password Again', required=True,
        widget=Fform.PasswordInput(attrs={'class':'form-control','placeholder':'Password Again'}),
    )
    username = Fform.CharField(
    max_length=200,required=True,help_text='Enter UserName',
    widget=Fform.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
    )
    email = Fform.EmailField(
    max_length=100,required=True,help_text='Enter Email Address',
    widget=Fform.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
    )
    first_name = Fform.CharField(
    max_length=100,required=True,help_text='Enter First Name',
    widget=Fform.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
    )

    last_name = Fform.CharField(
        max_length=100,required=True,help_text='Enter Last Name',
        widget=Fform.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
    )
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
