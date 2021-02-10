from django.urls import path

from .views import index_view
from .views import detail_view
from .views import cars_view


urlpatterns = [
    path('', index_view, name='index'),
    path('employee/<int:employee_id>/', detail_view, name='detail'),
    path('cars/<int:page>/', cars_view,name='cars')
]