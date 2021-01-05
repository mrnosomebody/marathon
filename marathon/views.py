from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView

from marathon.forms import *


def first_page(request):
    return render(request, 'first_page.html',{})

def race_creator(request):
    return render(request, 'race_creator/ConstructMarathon.html',{})

@login_required(login_url=reverse_lazy('m-login'))
def register_run(request, *args, **kwargs):
    user = Person.objects.get(pk=request.user.id)
    event = Event.objects.get(pk=request.POST['event_id'])
    run = Run(person_id=user, event_id=event)
    run.save()
    return HttpResponse()

def register_user(request):
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
            form._save_m2m()
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
            form._save_m2m()
            return redirect('m-login')
        else:
            messages.error(request, f'Error')
    else:
        form = Register_sponsor()
    return render(request, 'register/index.html', {'form': form})

def join(request):

    user = Person.objects.get()
    print(user)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/profile'
    template_name = 'login/index.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request,self.user)
        return super(LoginFormView,self).form_valid(form)

class EventListView(ListView):
    model = Event
    template_name = 'event/list_view.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/detail_view.html'






