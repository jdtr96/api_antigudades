from django.shortcuts import render
from django.db.models import Count, Avg

from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import Producto, Valoracion
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from producto.serializers import ProductoSerializer, ValoracionSerializer, ValoracionReadSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView


# Create your views here.


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        per = ["GET"]
        return request.method in per


def verificar_rol(request):
    token = request.headers["Authorization"].split()
    iduser = Token.objects.filter(
        key=token[1]
    ).values("user_id").first().get("user_id")
    rol = User.objects.filter(
        id=iduser
    ).values("ocupation").first().get("ocupation")
    return str(rol)


class ProductoViewsets(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    permission_classes = [IsAuthenticated | ReadOnly]

    def create(self, request, *args, **kwargs):
        if(verificar_rol(request) == "0"):
            serializer = ProductoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response({"Solo el administrador puede realizar la accion"})
        return Response(request.data)


class ValoracionViewsets(viewsets.ModelViewSet):
    serializer_class = ValoracionReadSerializer
    queryset = Valoracion.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if(verificar_rol(request) == "1"):
            serializer = ValoracionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response({"Solo el valuador puede realizar la accion"})
        return Response(request.data)


class AceptarVal(APIView):
    def get(self, request, *args, **kwargs):
        if(verificar_rol(request) == "0"):
            Valoracion.objects.filter(id=kwargs["pk"]).update(aceptada=True)
        else:
            return Response({"Solo el administrador puede realizar la accion"})

        return Response({"Valoracion Acceptada"})


class ValPro(APIView):
    def get(self, request, *args, **kwargs):
        if(verificar_rol(request) == "0"):
            reporte = Valoracion.objects.values('idProducto').filter(aceptada=True).order_by('idProducto').annotate(
                num_val=Count('idProducto'))
        else:
            return Response({"Solo el administrador puede realizar la accion"})

        return Response(reporte)


class ProValPro(APIView):
    def get(self, request, *args, **kwargs):
        if(verificar_rol(request) == "0"):
            reporte = Valoracion.objects.values('idProducto').filter(aceptada=True).order_by('idProducto').annotate(
                promedio_val=Avg('valor'))
        else:
            return Response({"Solo el administrador puede realizar la accion"})

        return Response(reporte)
