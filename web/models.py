from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=100)

    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



class Producto(models.Model):

    nombre = models.CharField(max_length=200)

    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    activo = models.BooleanField(default=True)

    novedad = models.BooleanField(default=False)

    creado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nombre