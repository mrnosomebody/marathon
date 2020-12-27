from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Distance(models.Model):
    distance = models.DecimalField(max_digits=4,decimal_places=2)

class Event(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=255)
    distance_id = models.ForeignKey(Distance, on_delete=models.PROTECT)

class Sponsor(models.Model):
    username = models.CharField(max_length=50)
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
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    time = models.TimeField()
    took_place = models.IntegerField()


