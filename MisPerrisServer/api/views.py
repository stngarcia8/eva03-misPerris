from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .funciones import getMascotasSerializer, getMascotaByIdSerializer, getMascotaByStatusSerializer, getPersonasSerializer, getAdopcionesSerializer


# Vista para mostrar todas las mascotas.
class MascotaView(APIView):

    # Metodo para obtener las mascotas.
    def get(self, request):
        return Response(getMascotasSerializer(None))


# Vista para mostrar una mascota por su identificador.
class MascotaViewById(APIView):

    # Metodo para obtener la mascota.
    def get(self, request, pk):
        return Response(getMascotaByIdSerializer(pk))


# Vista para mostrar mascotas filtradas por estado.
class MascotaByStatusView(APIView):

    # Metodo para obtener las mascotas.
    def get(self, request, estado):
        return Response(getMascotaByStatusSerializer(estado))


# Vista para mostrar las personas.
class PersonaView(APIView):

    # Obteniendo todas las personas registradas.
    def get(self, request):
        return Response(getPersonasSerializer(None))


# Vista para las adopciones.
class AdopcionView(APIView):

    # Obtener las adopciones.
    def get(self, request):
        return Response(getAdopcionesSerializer(None))
