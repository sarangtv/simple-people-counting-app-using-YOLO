from django import forms
from .models import *

class registerForm(forms.ModelForm):
    class Meta:
        model=registration
        fields=('username','password','email')
        widgets={
            'email':forms.TextInput(attrs={'class' :'form-control'}),
            'username':forms.TextInput(attrs={'class' :'form-control'}),
            'password':forms.TextInput(attrs={'class' :'form-control'}),
       
        }