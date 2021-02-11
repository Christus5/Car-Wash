from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('employee/<int:employee_id>/', detail_view, name='detail'),
    path('cars/<int:page>/', cars_view, name='cars'),
    path('employees/<int:page>/', employees_view, name='employees')
]