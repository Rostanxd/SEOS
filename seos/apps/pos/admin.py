from django.contrib import admin

# Register your models here.
from .models import Ciudad, Provincia

admin.site.register(Ciudad)
admin.site.register(Provincia)
