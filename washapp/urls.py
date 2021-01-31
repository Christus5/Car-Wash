from django.urls import path

from .views import index_view
from .views import detail_view


urlpatterns = [
    path('', index_view, name='index'),
    path('employee/<int:employee_id>/', detail_view, name='detail')
]