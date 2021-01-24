from django.contrib import admin

from .models import Employee
from .models import Permission
from .models import Role
from .models import Car
from .models import CarWashBooth


# Register your models here.
@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    readonly_fields = ['created']

admin.site.register([Permission, Role, Car, CarWashBooth])
