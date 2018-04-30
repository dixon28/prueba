from django.conf.urls import url, include
from apps.adopciones.views import *
urlpatterns = [
    url(r'^adopcion/', index),
    url(r'^soypior/',trap),
]
