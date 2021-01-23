from django.db import models

# Create your models here.


class Producto(models.Model):

    name = models.CharField(max_length=58, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    descripcion = models.CharField(max_length=58, blank=False, null=False)

    def __str__(self):
        return self.name


class Valoracion(models.Model):

    idProducto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='producto_valoracion'
    )
    referencia = models.CharField(max_length=58, blank=False, null=False)
    valor = models.DecimalField(
        decimal_places=4, max_digits=50, blank=False, null=False)
    aceptada = models.BooleanField(default=False)
