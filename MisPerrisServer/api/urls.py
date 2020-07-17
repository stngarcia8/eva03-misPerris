from django.conf.urls import url
from . import views


urlpatterns = [

    # Vistas para el tratamiento de las mascotas.
    url(r'^mascotas/$', views.MascotaView.as_view(), name='vistaMascotas'),
    url(r'^mascotaById/(?P<pk>\d+)/$',
        views.MascotaViewById.as_view(),
        name="mascotaById"),
    url(r'^mascotaByStatus/(?P<estado>\d+)/$',
        views.MascotaByStatusView.as_view(),
        name="mascotaByStatus"),

    # Vistas para el tratamiento de las personas.
    url(r'^personas/$', views.PersonaView.as_view(), name='vistaPersonas'),

    # Vistas para el tratamiento de las adopciones.
    url(r'^adopciones/$', views.AdopcionView.as_view(), name='vistaAdopciones'),

]
