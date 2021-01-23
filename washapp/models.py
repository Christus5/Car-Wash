from django.db import models


# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=100)

    role = models.ForeignKey(to='washapp.Role', on_delete=models.PROTECT)
    hired_date = models.DateField('Date Hired')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Added to DB')

    def __str__(self):
        return self.full_name


class Role(models.Model):
    title = models.CharField(max_length=50)
    salary = models.PositiveSmallIntegerField(verbose_name='Salary / Monthly')

    permissions = models.ManyToManyField(to='washapp.Permission')

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title


class Permission(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class CarWashBooth(models.Model):
    occupied = models.BooleanField(blank=True)
    occupant = models.ForeignKey(to='washapp.Employee', on_delete=models.PROTECT, null=True, blank=True)
    car = models.ForeignKey(to='washapp.Car', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    license_plate = models.CharField(max_length=7)

    def __str__(self):
        return self.license_plate