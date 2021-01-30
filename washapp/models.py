from django.db import models


# Create your models here.
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
    car = models.ForeignKey(to='Car', on_delete=models.PROTECT)
    wash_booth = models.ForeignKey(to='CarWashBooth', on_delete=models.PROTECT)
    washer = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    requested = models.DateTimeField()
    completed = models.DateTimeField()

    class Meta:
        unique_together = [['washer', 'wash_booth', 'requested', 'car']]

    def __str__(self):
        return self.car
