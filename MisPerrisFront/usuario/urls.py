from django.conf.urls import url
from django.urls import include

from . import views

# Definicion de las urls.
urlpatterns = [
    url(r'^listarDisponibles/$', views.listarDisponibles, name='listarDisponibles'),
]
