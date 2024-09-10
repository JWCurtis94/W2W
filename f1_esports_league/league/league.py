from django import forms
from .models import DriverProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['team', 'bio']