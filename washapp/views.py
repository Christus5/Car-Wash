from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.defaulttags import register

from .models import CarWashBooth
from .models import Car
from .models import Order
from .models import Employee

from .forms import OrderForm


@register.filter
def get_range(value):
    return range(value + 1)


# Create your views here.
def index_view(request, *args, **kwargs):
    orderForm = OrderForm()

    if request.POST:
        orderForm = OrderForm(request.POST)

        if orderForm.is_valid():
            orderForm.save()

    context = {
        'order_form': orderForm,
        'car_count': Car.objects.count(),
        'employee_count': Employee.objects.count()
    }

    return render(request, 'washapp/index.html', context)


def cars_view(request, page):
    return render(request, 'washapp/cars.html', {
        'cars': Car.objects.all()[page * 5:(5 * page) + 5],
        'current_page': page,
        'pages': int(Car.objects.count() / 5)
    })


def employees_view(request, page):
    search = request.GET.get('name')
    employee_q = Q()
    if search:
        employee_q &= Q(name__icontains=search) | Q(last_name__icontains=search)

    return render(request, 'washapp/employess.html', {
        'employees': Employee.objects.filter(employee_q)[page * 5:(page * 5) + 5],
        'current_page': page
    })


def detail_view(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'washapp/detail.html', {
        'employee': employee
    })
