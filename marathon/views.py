import math

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
    sponsors = Sponsor.objects.all().count()
    participants = Person.objects.all().count()
    races = Event.objects.all().count()
    return render(request, 'first_page.html', {'sponsors': sponsors, 'participants': participants, 'races': races})


@login_required(login_url=reverse_lazy('m-login'))
def register_run(request, *args, **kwargs):
    user = Person.objects.get(pk=request.user.id)
    event = Event.objects.get(pk=request.POST['event'])
    try:
        if Run.objects.get(person_id=user.id, event_id=event.id):
            messages.warning(request, ' Already exists ', fail_silently=False)
    except:
        run = Run(person=user, event=event)
        run.save()
    return HttpResponse()


@login_required(login_url=reverse_lazy('m-login'))
def register_run_sponsor(request, *args, **kwargs):
    sponsor = Sponsor.objects.get(pk=request.user.id)
    event = Event.objects.get(pk=request.POST['event'])
    event.sponsor_set.add(sponsor)
    return HttpResponse()


def my_runs(request):
    events = Event.objects.all()
    runs = Run.objects.get_queryset()
    print(events)
    return render(request, 'profile/my_runs.html', {'events': events, 'runs': runs})


def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('m-profile')
        else:
            messages.error(request, f'Error')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile/edit_profile.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
            form._save_m2m()
            return redirect('m-login')
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


def race_creator(request):
    if request.method == 'POST':
        form = RaceCreator(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.save()
            return redirect('m-event')
        else:
            messages.error(request, f'Error')
    else:
        form = RaceCreator()
    return render(request, 'race_creator/ConstructMarathon.html', {'form': form})

def show_sponsored(request):
    return render(request, 'event/list_view.html', {'events': Sponsor.objects.get(id=request.user.id).event_id.all()})

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'login/index.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'event/list_view.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/detail_view.html'

def marathon_info(request):
    count = Run.objects.count()
    events = {}
    id_arr = {}
    arr = []
    m = 0
    for element in Run.objects.all():
        if not (element.event.id in events):
            events[element.event.id] = {
                    'name': element.event.name,
                    'place': element.event.place,
                    'date': element.event.date,
                    'distance': element.event.distance.distance,
                    'participants': 0,
                    'id': element.event.id
                }
        events[element.event.id]['participants'] += 1
        arr.append(events[element.event.id]['participants'])

    events_array = []
    for n in events.values():
        events_array.append(n)


    runners_arr = []
    len = 0
    for pers in Person.objects.all():
        if pers.status_id.get().id == 1:
            runners_arr.append({'pers': pers, 'level': 0, 'place': 0})
            ex = 0.0
            r_count = Run.objects.filter(person=pers).count()
            for i in range(0, r_count):
                if Run.objects.filter(person=pers)[i].took_place != 0:
                    ex += 20 * math.log(int(Run.objects.filter(person=pers)[i].event.distance.distance)) / Run.objects.filter(person=pers)[i].took_place

            level = int(ex // 150)
            runners_arr[len]['level'] = level
            len+= 1

    runners_arr_sorted = sorted(runners_arr, key=lambda k: k['level'], reverse=True)
    for i in range(len):
        runners_arr_sorted[i]['place'] = i +1

    return render(request, 'info/marathon_info.html', {
        'events': events_array,
        'sponsors': Sponsor.objects.all(),
        'runners': runners_arr_sorted
    })