from django.urls import  include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listarRescatados/$', views.listarRescatados, name='listarRescatados' ),
]