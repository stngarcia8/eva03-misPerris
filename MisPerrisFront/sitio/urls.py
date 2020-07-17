from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.irInicio, name='irInicio'),
    url(r'^registrarPersona$', views.registrarPersona, name='registrarPersona'),
    url(r'^sinConexion/$', views.sinConexion, name='sinConexion' ),
]
