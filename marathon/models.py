from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Distance(models.Model):
    distance = models.DecimalField(max_digits=4,decimal_places=2)

class Event(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=255)
    distance = models.ForeignKey(Distance, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("m-event_detail", kwargs={'pk': self.pk})

class Sponsor(User):
    company = models.CharField(max_length=100 )
    phone_num = models.CharField(max_length=12)
    e_mail = models.CharField(max_length=50)
    event_id = models.ManyToManyField(Event)

class Status(models.Model):
    name = models.CharField(max_length=40)

class Person(User):
    third_name = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=12)
    status_id = models.ManyToManyField(Status)

class Run(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    time = models.IntegerField(default=0)
    took_place = models.IntegerField(default=0)


