from django.contrib import admin

from .models import *

@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    readonly_fields = ['created']

admin.site.register([Car, CarWashBooth, Order])
