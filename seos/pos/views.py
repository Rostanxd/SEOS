from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Provincia, Ciudad


def index(request):
    return HttpResponse("Hello, world. You're at the pos index.")


class ListProvinciaView(ListView):
    template_name = 'pos/provincias_list.html'
    context_object_name = 'provincias_list_all'

    def get_queryset(self):
        return Provincia.objects.all()


class ListCiudadesView(ListView):
    template_name = 'pos/ciudades_list.html'
    context_object_name = 'ciudades_list_all'

    def get_queryset(self):
        return Ciudad.objects.all()
