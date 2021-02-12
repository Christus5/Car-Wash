from django import forms

from .models import *


class OrderForm(forms.ModelForm):
    requested = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type': 'datetime-local'
    }))
    completed = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type': 'datetime-local'
    }))

    car = forms.ModelChoiceField(empty_label='Select Car', queryset=Car.objects.all())
    wash_booth = forms.ModelChoiceField(empty_label='Select Booth', queryset=CarWashBooth.objects.all())
    washer = forms.ModelChoiceField(empty_label='Select Washer', queryset=Employee.objects.all())
    price = forms.DecimalField(min_value=0)

    class Meta:
        model = Order
        fields = '__all__'
