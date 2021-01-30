from django.contrib import admin

from .models import Employee
from .models import Car
from .models import CarWashBooth
from .models import Order

@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    readonly_fields = ['created']

admin.site.register([Car, CarWashBooth, Order])
