from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UsuarioForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "sistema/usuario_new.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('pos:provincias_list')
