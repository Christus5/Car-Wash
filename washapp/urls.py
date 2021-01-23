from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('booth/<int:booth_id>', views.booth_view, name='booth'),
    path('dashboard/', views.dashboard_view, name='dashboard')
]