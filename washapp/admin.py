from django.contrib import admin

from .models import Employee
from .models import Car
from .models import CarWashBooth
from .models import Order
from .models import Company
from .models import BoothToCompany
from .models import EmployeeToCompany
from .models import OrderToCompany


# Register your models here.
class BoothToCompanyInline(admin.TabularInline):
    model = BoothToCompany
    extra = 0

class EmployeeToCompanyInline(admin.TabularInline):
    model = EmployeeToCompany
    extra = 0


class OrderToCompanyInline(admin.TabularInline):
    model = OrderToCompany
    extra = 0

@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    readonly_fields = ['created']


@admin.register(Company)
class CompanyAdminModel(admin.ModelAdmin):
    inlines = [BoothToCompanyInline, EmployeeToCompanyInline, OrderToCompanyInline]

admin.site.register([Car, CarWashBooth, Order])
