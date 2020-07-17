from django.conf import settings
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# listarRescatados: Vista para mostrar los perritos rescatados y poder mantener la informacion de estos.
@login_required(login_url='iniciarSesion')
def listarRescatados(request):
    if not request.user.is_superuser:
        return redirect('restringirAcceso')
    miPlantilla = loader.get_template("listarRescatados.html")
    return HttpResponse(miPlantilla.render({}, request))


