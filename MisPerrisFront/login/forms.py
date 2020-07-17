from django import forms
from django.forms import ModelForm


# Formulario de inicio de sesion.
class IniciarSesionForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(), label="Nombre de Usuario")
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Contraseña")
