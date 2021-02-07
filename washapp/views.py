from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import CarWashBooth
from .models import Car
from .models import Order
from .models import Employee

from .forms import OrderForm


# Create your views here.
def index_view(request, *args, **kwargs):
    orderForm = OrderForm()

    if request.POST:
        orderForm = OrderForm(request.POST)

        if orderForm.is_valid():
            orderForm.save()

    search = request.GET.get('name')
    employee_q = Q()
    if search:
        employee_q &= Q(name__icontains=search) | Q(last_name__icontains=search)

    context = {
        'employees': Employee.objects.filter(employee_q),
        'order_form': orderForm
    }

    return render(request, 'washapp/index.html', context)


def detail_view(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'washapp/detail.html', {
        'employee': employee
    })
