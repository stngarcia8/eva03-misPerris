from django.conf import settings
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .forms import IniciarSesionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


# iniciarSesion: Vista para el inicio de sesion.
def iniciarSesion(request):
    form = IniciarSesionForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            username=data.get("username"), password=data.get("password"))
        if user is not None:
            login(request, user)
            return redirect('irInicio')
        else:
            return redirect('denegarAcceso')
    return render(request, "iniciarSesion.html", {'form': form})


# cerrarSesion:  Vista para cerrar la sesion.
# Retorna: Redirecciona a la pagina de inicio.
@login_required(login_url='iniciarSesion')
def cerrarSesion(request):
    logout(request)
    return redirect('/')


# denegarAcceso: Vista para carga la plantilla que indica error de login.
def denegarAcceso(request):
    miPlantilla = loader.get_template("denegarAcceso.html")
    return HttpResponse(miPlantilla.render({}, request))


# restringirAcceso: Vista para cargar ls plantilla de acceso restringido.
def restringirAcceso(request):
    miPlantilla = loader.get_template("restringirAcceso.html")
    return HttpResponse(miPlantilla.render({}, request))


def settings(request):
    user = request.user
    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    return render(request, 'core/settings.html', {
        'github_login': github_login,
        'can_disconnect': can_disconnect
    })