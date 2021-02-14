from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.defaulttags import register
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Car
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


def cars_view(request, *args, **kwargs):
    cars_list = Car.objects.all()

    paginator = Paginator(cars_list, 3)
    page = request.GET.get('page')

    try:
        cars = paginator.page(page)
    except:
        HttpResponseRedirect('?page=1')

    return render(request, 'washapp/cars.html', {
        'cars': cars,
        'page': paginator.page(page)
    })


def employees_view(request, *args, **kwargs):
    search = request.GET.get('name')
    employee_q = Q()
    if search:
        employee_q &= Q(name__icontains=search) | Q(last_name__icontains=search)
    employees_list = Employee.objects.filter(employee_q)

    paginator = Paginator(employees_list, 3)
    page = request.GET.get('page')

    try:
        employees = paginator.page(page)
    except:
        return HttpResponseRedirect(f'?page=1&name={search}')

    return render(request, 'washapp/employess.html', {
        'employees': employees,
        'page': paginator.page(page),
    })


def detail_view(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'washapp/employee_detail.html', {
        'employee': employee
    })
