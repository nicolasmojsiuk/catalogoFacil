from django.contrib import admin
from .models import Producto, Categoria
from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.unregister(User)
admin.site.unregister(Group)
