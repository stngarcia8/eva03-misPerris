from rest_framework import serializers
from .models import Mascota, Persona, Adopcion
from django.conf import settings


# Serializador para el modelo Mascota.
class MascotaSerializer(serializers.ModelSerializer):

    # para obtener la ruta de la imagen.
    ruta_imagen = serializers.SerializerMethodField()
    class Meta:
        model = Mascota
        fields = ('id', 'nombre', 'raza', 'estado',
                  'descripcion', 'ruta_imagen')
    # para encodear la ruta de la imagen.
    def get_ruta_imagen(self, object):
        return '%s%s' % (settings.MEDIA_URL.replace('\\', '/'), object.imagen.name)



# Serializador para el modelo Persona.
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('__all__')


# Serializador para las adopciones.
class AdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcion
        fields = ('__all__')
