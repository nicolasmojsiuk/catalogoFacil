from django.shortcuts import render
from .models import Producto, Categoria

def inicio(request):

    categorias = Categoria.objects.filter(activa=True)

    categoria_id = request.GET.get("categoria")
    if categoria_id:
        productos = Producto.objects.filter(activo=True, categoria__id=categoria_id)
    else:
        productos = Producto.objects.filter(activo=True)

    novedades = Producto.objects.filter(activo=True, novedad=True)

    return render(request, "index.html", {
        "productos": productos,
        "novedades": novedades,
        "categorias": categorias,
    })