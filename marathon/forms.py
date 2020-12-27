from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from marathon.models import *

STATUS_CHOICES = [(1, 'Runner'), (2, 'Coordinator'), (3, 'Organizer')]
SEX_CHOICES = [(1, 'Male'), (2, 'Female')]


class Register_user(UserCreationForm):
    status_id = forms.ChoiceField(widget=forms.Select, choices=STATUS_CHOICES)
    sex = forms.ChoiceField(widget=forms.Select, choices=SEX_CHOICES)

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


class Register_sponsor(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Sponsor
        fields = ["username", "e_mail", "password", "company", "phone_num"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
