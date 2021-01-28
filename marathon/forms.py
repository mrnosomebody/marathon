from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from marathon.models import *

STATUS_CHOICES = [(1, 'Runner'), (2, 'Organizer'), (3, 'Coordinator')]
SEX_CHOICES = [("Male", 'Male'), ("Female", 'Female')]
DISTANCES = [(1, 5.0), (2, 10.0), (3, 21.1), (4, 42.2)]


class Register_user(UserCreationForm):
    status_id = forms.ChoiceField(widget=forms.Select, choices=STATUS_CHOICES, required=True)
    sex = forms.ChoiceField(widget=forms.Select, choices=SEX_CHOICES, required=True)

    class Meta:
        model = Person
        fields = ["username", "email", "first_name", "last_name", "third_name", "sex", "phone_num",
                  "status_id"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Пользователь с таким email уже существует. Пожалуйста укажите другой email")


class Register_sponsor(UserCreationForm):
    class Meta:
        model = Sponsor
        fields = ["username", "e_mail", "company", "phone_num"]


class RaceCreator(ModelForm):
    distance = forms.ChoiceField(widget=forms.Select, choices=DISTANCES, required=True, label="Distance")

    class Meta:
        model = Event
        fields = ["name", "place", "date", "distance"]

    def clean_distance(self):
        distance_id = int(self.cleaned_data['distance'])
        distance = Distance.objects.get(id=distance_id)
        return distance


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'third_name', 'email', 'phone_num']

