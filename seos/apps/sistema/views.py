from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UsuarioForm


@login_required
def InicioSesion(request):
    user = None
    if request.user.is_authenticated():
        user = request.user

    return render(request, 'main.html', {'user': user})


class RegistroUsuario(CreateView):
    model = User
    template_name = "sistema/usuario_new.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('pos:provincias_list')
