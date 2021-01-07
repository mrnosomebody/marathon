from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', profile, name = 'm-profile'),
    path('sponsor-profile/', sponsor_profile, name = 'm-sponsor-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='first_page.html'), name='m-logout'),
]