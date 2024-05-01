from django import forms
from .models import data

class theform(forms.ModelForm):
    class Meta: 
        model=data
        fields=['Name','RegNo','Mark1','Mark2','Mark3']

