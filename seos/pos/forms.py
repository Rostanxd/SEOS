from django import forms

from .models import Provincia, Ciudad


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ('codigo', 'nombre', 'area', )


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ('codigo', 'nombre', 'provincia', )
