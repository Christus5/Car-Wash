from django.shortcuts import render

from .models import (CarWashBooth, Car)


# Create your views here.
def index_view(request, *args, **kwargs):

    context = {
        'booths': CarWashBooth.objects.filter(occupied=False),
        'cars': Car.objects.all()
    }
    return render(request, 'washapp/index.html', context)