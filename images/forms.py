from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['posted_by','profile','likes']
