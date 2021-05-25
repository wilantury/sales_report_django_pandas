# Django
from django import forms

# Models
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model =  Profile
        exclude = ('user',)