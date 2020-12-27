from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from marathon.forms import *


def first_page(request):
    return render(request, 'first_page.html',{})


def register_user(request):

    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yor account has been created. Now you can Log In')
            return redirect('first_page')
        else:
            messages.error(request, f'Error')
    else:
        form = Register_user()
    return render(request, 'register/index.html', {'form': form})

def register_sponsor(request):

    if request.method == 'POST':
        form = Register_sponsor(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yor account has been created. Now you can Log In')
            return redirect('first_page')
        else:
            messages.error(request, f'Error')
    else:
        form = Register_sponsor()
    return render(request, 'register/index.html', {'form': form})
