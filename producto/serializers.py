from rest_framework import serializers
from producto.models import Producto, Valoracion


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'


class ValoracionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Valoracion
        fields = ['idProducto', 'referencia', 'valor']


class ValoracionReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Valoracion
        fields = '__all__'
