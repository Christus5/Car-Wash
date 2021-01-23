from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    attributes = {
        'placeholder': "AA000AA"
    }
    license_plate = forms.CharField(label='',min_length=7, max_length=7, widget=forms.TextInput(attrs=attributes))

    class Meta:
        model = Car
        fields = [
            'license_plate'
        ]
