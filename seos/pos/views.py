from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Provincia, Ciudad

from .forms import ProvinciaForm, CiudadForm


def index():
    return HttpResponse("Hello, world. You're at the pos index.")


def provincia_new(request):
    if request.method == "POST":
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            provincia = form.save()
            provincia.save()
            return redirect('pos:provincia_detail', pk=provincia.pk)
    else:
        form = ProvinciaForm()
    return render(request, 'pos/provincia_edit.html', {'form':form})


def provincia_detail(request, pk):
    provincia = get_object_or_404(Provincia, pk=pk)
    return render(request, 'pos/provincia_detail.html', {'provincia': provincia})


def provincia_edit(request, pk):
    provincia = get_object_or_404(Provincia, pk=pk)
    if request.method == "POST":
        form = ProvinciaForm(data=request.POST, instance=provincia)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('pos:provincia_detail', pk=post.pk)
        else:
            print('No valid form.')
    else:
        form = ProvinciaForm(instance=provincia)
    return render(request, 'pos/provincia_edit.html', {'provincia': provincia})


def ciudad_new(request):
    provincias = Provincia.objects.all()
    if request.method == "POST":
        form = CiudadForm(request.POST)
        if form.is_valid():
            ciudad = form.save()
            ciudad.save()
            return redirect('pos:ciudad_detail', pk=ciudad.pk)
    else:
        form = CiudadForm()
    return render(request, 'pos/ciudad_edit.html', {'form':form, 'provincias': provincias})


def ciudad_detail(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    return render(request, 'pos/ciudad_detail.html', {'ciudad': ciudad})


def ciudad_edit(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    provincias = Provincia.objects.all()
    if request.method == "POST":
        form = CiudadForm(data=request.POST, instance=ciudad)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('pos:ciudad_detail', pk=post.pk)
        else:
            print('No valid form.')
    else:
        form = CiudadForm()
    return render(request, 'pos/ciudad_edit.html', {'ciudad': ciudad, 'provincias': provincias})


class ListProvinciaView(ListView):
    model = Provincia
    template_name = 'pos/provincias_list.html'
    context_object_name = 'provincias_list_all'
    paginate_by = 10

    def get_queryset(self):
        return Provincia.objects.all().order_by('nombre')


class DetailProvinciaView(DetailView):
    model = Provincia
    template_name = 'pos/provincia_detail.html'

    def get_queryset(self):
        return Provincia.objects.all()


class CreateProvinciaView(CreateView):
    model = Provincia
    fields = '__all__'
    template_name = 'pos/provincia_edit.html'

    def get_success_url(self):
        return reverse('provincias_list')


class ListCiudadesView(ListView):
    model = Ciudad
    template_name = 'pos/ciudades_list.html'
    context_object_name = 'ciudades_list_all'
    paginate_by = 15

    def get_queryset(self):
        return Ciudad.objects.all().order_by('nombre')


class DetailCiudadView(DetailView):
    model = Ciudad
    template_name = 'pos/ciudad_detail.html'


class CreateCiudadView(CreateView):
    model = Ciudad
    fields = '__all__'
    # template_name = 'pos/ciudad_edit.html'

    def get_success_url(self):
        return reverse('ciudades_list')
