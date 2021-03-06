from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.defaulttags import register
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Car
from .models import Employee

from .forms import OrderForm


@register.filter
def get_range(value):
    return range(value + 1)


# Create your views here.
def index_view(request, *args, **kwargs):
    order_form = OrderForm()

    if request.POST:
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_form.save()

    context = {
        'order_form': order_form,
        'car_count': Car.objects.count(),
        'employee_count': Employee.objects.count()
    }

    return render(request, 'washapp/index.html', context)


def cars_view(request, *args, **kwargs):
    cars_list = Car.objects.all()

    paginator = Paginator(cars_list, 3)
    page = request.GET.get('page')
    cars = []

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
        return HttpResponseRedirect(f'?page=1&name={search}' if search else '?page=1')

    return render(request, 'washapp/employees.html', {
        'employees': employees,
        'page': paginator.page(page),
    })


def detail_view(request, *args, **kwargs):
    employee = get_object_or_404(Employee, pk=kwargs['employee_id'])


    orders_by = request.GET.get('orders_by')
    orders = employee.order_set.all()
    if orders_by == 'day':
        orders = [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(days=1)]
    elif orders_by == 'week':
        orders = [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(weeks=1)]
    elif orders_by == 'month':
        orders = [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(weeks=4)]

    paginator = Paginator(orders, 5)
    page = request.GET.get('page')

    try:
        orders = paginator.page(page)
    except:
        return HttpResponseRedirect(f'?page=1&orders_by={orders_by}' if orders_by else '?page=1')



    return render(request, 'washapp/employee_detail.html', {
        'employee': employee,
        'orders': orders,
        'page': paginator.page(page)
    })
