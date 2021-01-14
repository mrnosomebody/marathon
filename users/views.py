import math
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from marathon.models import *


@login_required(login_url=reverse_lazy('m-login'))
def profile(request):
    user = Person.objects.get(username=request.user.username)
    ex = 0.0
    r_count = Run.objects.filter(person=user).count()
    for i in range(0, r_count):
        if Run.objects.filter(person=user)[i].took_place != 0:
            ex += 20 * math.log(int(Run.objects.filter(person=user)[i].event.distance.distance)) / \
                  Run.objects.filter(person=user)[i].took_place

    level = int(ex // 150)
    my_experience = int(ex % 150)
    pg_experience = int(((ex % 150) / 150) * 100)
    if pg_experience < 3:
        pg_experience = 3

    left = 150 * (level)
    right = 150 * (level + 1)
    return render(request, 'profile/user_profile.html', {'user': user, 'level': level, 'my_experience': my_experience,
                                                         'pg_experience': pg_experience, 'left': left, 'right': right})


@login_required(login_url=reverse_lazy('m-login'))
def sponsor_profile(request):
    user = Sponsor.objects.get(username=request.user.username)
    print(user.email)
    return render(request, 'profile/sponsor_profile.html', {'user': user})
