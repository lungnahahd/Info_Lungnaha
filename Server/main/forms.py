from django import forms
from .models import infolist

class infopost(forms.ModelForm):
    class Meta:
        model = infolist
        fields = ['title', 'information']
        