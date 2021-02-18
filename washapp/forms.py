from django import forms

from .models import *


class OrderForm(forms.ModelForm):
    requested = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type': 'datetime-local'
    }))
    completed = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type': 'datetime-local'
    }), label='When to be completed')

    car = forms.ModelChoiceField(empty_label='Select Car', queryset=Car.objects.all())
    wash_booth = forms.ModelChoiceField(empty_label='Select Booth', queryset=CarWashBooth.objects.all())
    washer = forms.ModelChoiceField(empty_label='Select Washer',
                                    queryset=Account.objects.filter(is_staff=True, is_admin=False))
    price = forms.DecimalField(min_value=0)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        if user.type == 'customer':
            self.fields = {'completed': self.fields['completed'], 'car': forms.ModelChoiceField(
                empty_label='Select Car',
                queryset=user.car_set.filter(is_active=True)
            )}


    class Meta:
        model = Order
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('license_plate',)
