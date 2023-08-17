from django import forms



class Curso_form(forms.Form):
    nombre =  forms.CharField(max_length=40)
    comision = forms.IntegerField()