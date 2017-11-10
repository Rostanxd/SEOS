from django.conf.urls import url

from .views import RegistroUsuario, InicioSesion

app_name = 'sistema'

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    url(r'^$', InicioSesion, name='main'),
]
