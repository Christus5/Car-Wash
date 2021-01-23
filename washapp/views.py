from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import (CarWashBooth, Car)
from .forms import CarForm


# Create your views here.
def index_view(request, *args, **kwargs):

    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('dashboard')

    context = {
        'booths': len(CarWashBooth.objects.filter(occupied=False)),
        'working': True,
        'car_form': form
    }
    return render(request, 'washapp/index.html', context)

def dashboard_view(request, *args, **kwargs):
    context = {
        'cars': Car.objects.all(),
        'booths': CarWashBooth.objects.filter(occupied=False)
    }
    return render(request, 'washapp/dashboard.html', context)

def booth_view(request, *args, **kwargs):
    return render(request, 'washapp/booth.html', {
        'booth': kwargs['booth_id']
    })
