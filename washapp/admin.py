from django.contrib import admin

from .models import (
    Employee, Permission, Role,
    Car, CarWashBooth
)


# Register your models here.
@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    readonly_fields = ['created']

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Car)
admin.site.register(CarWashBooth)
