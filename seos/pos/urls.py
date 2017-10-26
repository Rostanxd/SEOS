from django.conf.urls import url

from . import views

app_name = 'pos'

urlpatterns = [
    url(r'^provincias/$', views.ListProvinciaView.as_view(), name='provincias_list'),
    url(r'^ciudades/$', views.ListCiudadesView.as_view(), name='ciudades_list'),
    url(r'^$', views.index, name='index'),
]