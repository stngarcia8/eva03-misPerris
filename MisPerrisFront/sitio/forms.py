from django import forms


# Formulario de filtros de galeria de perritos.
class filtrarGaleriaForm(forms.Form):

    # opciones de tipos de mascotas.
    tipos = ((8, 'Todas las mascotas'), (16, 'Rescatados'),
             (32, 'Disponibles'), (64, 'Adoptados'))

    # creando el campo de los estados.
    estado = forms.ChoiceField(choices=tipos)
