from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    booths = models.ManyToManyField(to='washapp.CarWashBooth', related_name='booths', through='washapp.BoothToCompany')
    employees = models.ManyToManyField(to='washapp.Employee', through='washapp.EmployeeToCompany')
    orders = models.ManyToManyField(to='washapp.Order', through='washapp.OrderToCompany')

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class BoothToCompany(models.Model):
    company = models.ForeignKey(to='washapp.Company', on_delete=models.PROTECT)
    booth = models.OneToOneField(to='washapp.CarWashBooth', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booth"
        verbose_name_plural = "Booths"


class EmployeeToCompany(models.Model):
    employee = models.OneToOneField(to='washapp.Employee', on_delete=models.CASCADE)
    company = models.ForeignKey(to='washapp.Company', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class OrderToCompany(models.Model):
    order = models.OneToOneField(to='washapp.Order', on_delete=models.CASCADE)
    company = models.ForeignKey(to='washapp.Company', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Employee(models.Model):
    full_name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Hired')

    def __str__(self):
        return self.full_name


class CarWashBooth(models.Model):
    occupied = models.BooleanField(blank=True)
    occupant = models.OneToOneField(to='washapp.Employee', on_delete=models.PROTECT, null=True, blank=True)
    car = models.OneToOneField(to='washapp.Car', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    license_plate = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.license_plate


class Order(models.Model):
    car = models.ForeignKey(to='washapp.Car', on_delete=models.PROTECT)
    wash_booth = models.ForeignKey(to='washapp.CarWashBooth', on_delete=models.PROTECT)
    washer = models.ForeignKey(to='washapp.Employee', on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    requested = models.DateTimeField()
    completed = models.DateTimeField()

    class Meta:
        unique_together = [['washer', 'wash_booth', 'requested', 'car']]

    def __str__(self):
        return str(self.pk)
