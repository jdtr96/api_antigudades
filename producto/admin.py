from django.contrib import admin

# Register your models here.

from .models import Producto, Valoracion

admin.site.register(Producto)
admin.site.register(Valoracion)
