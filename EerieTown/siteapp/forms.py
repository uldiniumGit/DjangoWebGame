from django.contrib.auth.forms import UserCreationForm
from .models import GameUser
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = GameUser
        fields = ('username', 'password1', 'password2', 'email')
