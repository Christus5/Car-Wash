from django.urls import path

from users.views import *
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'washapp'

urlpatterns = [
    path('', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),

    path('home/', index_view_router, name='index'),
    path('employee/<int:employee_id>/', detail_view, name='detail'),
    path('cars/', cars_view, name='cars'),
    path('employees/', employees_view, name='employees'),


]
