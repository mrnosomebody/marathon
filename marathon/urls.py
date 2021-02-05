from django.urls import path
from .views import *

urlpatterns = [
    path('',first_page,name = "first_page"),
    path('login/', LoginFormView.as_view(),name = "m-login"),
    path('registeruser/', register_user,name = "m-register-user"),
    path('registersponsor/', register_sponsor,name = "m-register-sponsor"),
    path('event/', EventListView.as_view(), name='m-event'),
    path('event/<int:pk>/', EventDetailView.as_view(),  name='m-event_detail'),
    path('join/',register_run,name='join'),
    path('join-sponsor/',register_run_sponsor,name='join-sponsor'),
    path('race-creator/', race_creator, name='race-creator'),
    path('my-runs/', my_runs, name='my-runs'),
    path('user-editor/', user_update, name='m-profile-editor'),
    path('m-info/', marathon_info, name='m-info'),
    path('my-sponsored/', show_sponsored, name='m-event_sponsored'),
]
