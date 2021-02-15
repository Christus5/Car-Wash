from django.urls import path

from .views import *

app_name = 'washapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('employee/<int:employee_id>/', detail_view, name='detail'),
    path('cars/', cars_view, name='cars'),
    path('employees/', employees_view, name='employees')
]
