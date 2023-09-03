from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class Curso_form(forms.Form):
    nombre =  forms.CharField(max_length=40)
    comision = forms.IntegerField()



class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contrasenia", widget=forms.TextInput)
    password2 = forms.CharField(label="Repetir la contrasenia", widget=forms.TextInput)


    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_text = {k:"" for k in fields}


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password", 
        widget=forms.TextInput, 
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.TextInput,
    )
