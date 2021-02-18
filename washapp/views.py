from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import register

from .forms import *


@register.filter
def get_range(value):
    return range(value + 1)


def index_view(request, *args, **kwargs):
    user = request.user

    order_form = OrderForm(user=user)

    if request.POST:
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_form.save()

    context = {
        'order_form': order_form,
        'car_count': Car.objects.filter(owner=user).count(),
        'employee_count': Account.objects.filter(is_staff=True, is_admin=False).count()
    }

    return render(request, 'washapp/index/index.html', context)


def index_view_customer(request, *args, **kwargs):
    cars = request.user.car_set.all()

    order_form = OrderForm(user=request.user)

    return render(request, 'washapp/index/index_customer.html', {
        'car_count': cars.count(),
        'cars': cars,
        'order_form': order_form,
        'messages': get_messages(request)

    })


@login_required
def index_view_router(request, *args, **kwargs):
    view = {
        'customer': index_view_customer(request, *args, **kwargs),
        'employee': index_view(request, *args, **kwargs),
        'employer': index_view(request, *args, **kwargs)
    }

    return view.get(getattr(request.user, 'type', None), index_view_customer(request, *args, **kwargs))


@login_required
def cars_view(request, *args, **kwargs):
    user = request.user
    cars_list = user.car_set.all().order_by('owner__car__license_plate')

    car_form = CarForm()

    if request.method == 'POST':
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            license_plate = car_form.save(commit=False)
            Car.objects.create(license_plate=license_plate, owner=user)
            return redirect('washapp:index')

    paginator = Paginator(cars_list, 3)
    page = request.GET.get('page')
    cars = []

    try:
        cars = paginator.page(page)
    except:
        HttpResponseRedirect('?page=1')

    return render(request, 'washapp/cars.html', {
        'cars': cars,
        'car_form': car_form,
        'page': paginator.page(page)
    })


def delete_car(request, *args, **kwargs):
    car_id = kwargs['pk']
    user = request.user
    try:
        car = user.car_set.get(pk=car_id)
    except:
        messages.add_message(request, 40, "Couldn't find car!")
        return redirect(to='washapp:index')

    if car is not None:
        car.delete()

    return redirect(to='washapp:index')


@login_required
def employees_view(request, *args, **kwargs):
    search = request.GET.get('name')
    employee_q = Q()
    if search:
        employee_q &= Q(name__icontains=search) | Q(last_name__icontains=search)
    employees_list = Account.objects.filter(employee_q, is_staff=True, is_admin=False).order_by('last_name')

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


@login_required
def detail_view(request, *args, **kwargs):
    if not request.user.is_staff:
        return redirect(to='washapp:index')
    employee = get_object_or_404(Account, pk=kwargs['employee_id'])

    orders_by = request.GET.get('orders_by')
    orders = employee.order_set.all()
    if orders_by == 'day':
        orders = [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(days=1)]
    elif orders_by == 'week':
        orders = [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(weeks=1)]
    elif orders_by == 'month':
        orders = [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(weeks=4)]

    paginator = Paginator(orders.order_by('id'), 5)
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


@login_required
def inbox_view(request, *args, **kwargs):
    if not request.user.is_superuser:
        return redirect(to='washapp:index')

    cars = Car.objects.filter(is_active=False)

    if request.method == 'POST':
        car = Car.objects.get(pk=request.POST['car_id'])
        car.is_active = True
        car.save()

    return render(request, 'washapp/inbox/admin_inbox.html', {
        'cars': cars
    })
