from django import forms
from .models import orders
from django.contrib.auth.models import User


class order_form(forms.ModelForm):
    
    class Meta:
        model= orders
        fields='__all__'

class signup(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','password']

class signup2(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','password']
