from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from marathon.models import *


def profile(request):
    user = Person.objects.get(username=request.user.username)
    #status = Status.objects.get(pk= user.status_id)
    return render(request, 'profile/user_profile.html', {'user':user})