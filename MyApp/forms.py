from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Curso_form(forms.Form):
    nombre =  forms.CharField(max_length=40)
    comision = forms.IntegerField()



class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contrasenia", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_text = {k:"" for k in fields}