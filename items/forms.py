from django import forms
from .models import Complain

class QuantityForm(forms.Form):
    quantity=forms.IntegerField(max_value=100,min_value=1)

    class Meta:
        fields=['quantity']

class ComplainForm(forms.ModelForm):
    class Meta:
        model=Complain
        fields=["rate","text"]