from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('password_reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset/password_reset.html',
         ),
         name='reset_password'
         ),
    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]
