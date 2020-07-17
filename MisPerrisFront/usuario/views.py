from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)
from django.template import RequestContext, loader


# listarDisponibles: Vista para mostrar los perritos disponibles.
@login_required(login_url='iniciarSesion')
def listarDisponibles(request):
    if  request.user.is_superuser:
        return redirect('restringirAcceso')
    miPlantilla = loader.get_template("listarDisponibles.html")
    return HttpResponse(miPlantilla.render({}, request))
