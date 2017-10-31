from django.conf.urls import url

from . import views

app_name = 'pos'

urlpatterns = [
    url(r'^provincias/$', views.ListProvinciaView.as_view(), name='provincias_list'),
    url(r'^provincia/new', views.provincia_new, name='provincia_new'),
    url(r'^provincia/(?P<pk>[0-9]+)/$', views.provincia_detail, name='provincia_detail'),
    url(r'^provincia/(?P<pk>[0-9]+)/edit/$', views.provincia_edit, name='provincia_edit'),
    url(r'^ciudades/$', views.ListCiudadesView.as_view(), name='ciudades_list'),
    url(r'^ciudad/new', views.ciudad_new, name='ciudad_new'),
    url(r'^ciudad/(?P<pk>[0-9]+)/$', views.ciudad_detail, name='ciudad_detail'),
    url(r'^ciudad/(?P<pk>[0-9]+)/edit/$', views.ciudad_edit, name='ciudad_edit'),
    url(r'^$', views.index, name='index'),
]
