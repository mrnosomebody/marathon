from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from marathon.forms import *


def first_page(request):
    return render(request, 'first_page.html',{})


def register_user(request):
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('m-login')
        else:
            messages.error(request, f'Error')
    else:
        form = Register_sponsor()
    return render(request, 'register/index.html', {'form': form})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/admin'
    template_name = 'login/index.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request,self.user)
        return super(LoginFormView,self).form_valid(form)