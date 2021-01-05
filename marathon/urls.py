from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',first_page,name = "first_page"),
    path('login/', LoginFormView.as_view(),name = "m-login"),
    path('registeruser/', register_user,name = "m-register-user"),
    path('registersponsor/', register_sponsor,name = "m-register-sponsor"),
    path('event/', EventListView.as_view(), name='m-event'),
    path('event/<int:pk>/', EventDetailView.as_view(),  name='m-event_detail'),
    path('join/',register_run,name='join'),
    path('race-creator/', race_creator, name='race-creator')

]
