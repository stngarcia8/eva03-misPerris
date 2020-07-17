from django.conf import settings
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .forms import filtrarGaleriaForm


def irInicio(request):
    if request.method == 'POST':
        miForm = filtrarGaleriaForm(request.POST)
    else:
        miForm = filtrarGaleriaForm()
    miPlantilla = loader.get_template("index.html")
    miContexto = {'form': miForm}
    return HttpResponse(miPlantilla.render(miContexto, request))


def registrarPersona(request):
    miPlantilla = loader.get_template("index.html")
    return HttpResponse(miPlantilla.render({}, request))


# sinConexion: Vista para cargar ls plantilla de trabajar sin conexion.
def sinConexion(request):
    miPlantilla = loader.get_template("trabajarSinConexion.html")
    return HttpResponse(miPlantilla.render({}, request))