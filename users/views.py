from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from marathon.models import *

@login_required
def profile(request):
    user = Person.objects.get(username=request.user.username)
    return render(request, 'profile/user_profile.html', {'user':user})

@login_required
def sponsor_profile(request):
    user = Sponsor.objects.get(username=request.user.username)
    print(user.email)
    return render(request, 'profile/sponsor_profile.html', {'user':user})