from django.db import models
from django.utils import timezone

from users.models import Account


class CarWashBooth(models.Model):
    occupied = models.BooleanField(blank=True)
    occupant = models.OneToOneField(Account, on_delete=models.PROTECT, null=True, blank=True)
    car = models.OneToOneField(to='washapp.Car', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Booth"
        verbose_name_plural = "Booths"

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    license_plate = models.CharField(max_length=7, unique=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_plate


class Order(models.Model):
    STATUS = (
        ('Completed', "Completed"),
        ('Pending', "Pending")
    )

    car = models.ForeignKey(to='Car', on_delete=models.PROTECT)
    wash_booth = models.ForeignKey(to='CarWashBooth', on_delete=models.PROTECT)
    washer = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(choices=STATUS, max_length=100, default='Pending')
    requested = models.DateTimeField()
    completed = models.DateTimeField()

    class Meta:
        unique_together = [['washer', 'wash_booth', 'requested', 'car']]

    def __str__(self):
        return f"{self.car} : {self.requested.date()}"
