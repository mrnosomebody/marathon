import math
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from marathon.models import *

def profile(request,username):
    user = get_object_or_404(Person, username=username)
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


def sponsor_profile(request,username):
    user = get_object_or_404(Sponsor, username=username)
    print(user.email)
    return render(request, 'profile/sponsor_profile.html', {'user': user})
