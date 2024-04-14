from django import forms
from .models import details

class theform(forms.ModelForm):
    class Meta: 
        model=details
        fields=['Name','Mark1','mark2']