from django import forms
from .models import *

class Support(forms.ModelForm):
    class Meta:
        model = Support
        fields = '__all__'

