from django import forms

class ingresarRescatadoForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(),required=True)
    raza=forms.CharField(widget=forms.TextInput(),required=True)
    imagen=forms.ImageField()
    descripcion=forms.CharField(widget=forms.Textarea(),required=True)
