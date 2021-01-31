from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import CarWashBooth
from .models import Car
from .forms import CarForm
from .models import Order
from .models import Employee


# Create your views here.
def index_view(request, *args, **kwargs):

    context = {
        'employees': Employee.objects.all()
    }
    return render(request, 'washapp/index.html', context)

def detail_view(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'washapp/detail.html', {
        'employee': employee
    })