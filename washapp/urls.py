from django.urls import path

from .views import *

app_name = 'washapp'

urlpatterns = [
    path('home/', index_view_router, name='index'),
    path('employee/<int:employee_id>/', detail_view, name='detail'),
    path('cars/', cars_view, name='cars'),
    path('employees/', employees_view, name='employees'),
    path('inbox', inbox_view, name='inbox'),
    path('delete_car/<int:pk>', delete_car, name='delete_car')
]
