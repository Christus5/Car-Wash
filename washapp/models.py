from django.db import models
from django.utils import timezone


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(default='washapp/no_image.svg', upload_to='washapp/employees/')
    share = models.PositiveSmallIntegerField(default=45)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Hired')

    def orders_by_day(self):
        orders = self.order_set.all()
        return [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(days=1)]

    def orders_by_week(self):
        orders = self.order_set.all()
        return [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(days=7)]

    def orders_by_month(self):
        orders = self.order_set.all()
        return [order for order in orders if order.completed >= timezone.now() - timezone.timedelta(days=30)]

    def __str__(self):
        return f"{self.name}  {self.last_name}"


class CarWashBooth(models.Model):
    occupied = models.BooleanField(blank=True)
    occupant = models.OneToOneField(to='washapp.Employee', on_delete=models.PROTECT, null=True, blank=True)
    car = models.OneToOneField(to='washapp.Car', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Booth"
        verbose_name_plural = "Booths"

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    license_plate = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.license_plate


class Order(models.Model):
    STATUS = (
        ('Completed', "Completed"),
        ('Pending', "Pending")
    )

    car = models.ForeignKey(to='Car', on_delete=models.PROTECT)
    wash_booth = models.ForeignKey(to='CarWashBooth', on_delete=models.PROTECT)
    washer = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(choices=STATUS, max_length=100, default='Pending')
    requested = models.DateTimeField()
    completed = models.DateTimeField()

    class Meta:
        unique_together = [['washer', 'wash_booth', 'requested', 'car']]

    def __str__(self):
        return f"{self.car} : {self.requested.date()}"
