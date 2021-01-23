from django.shortcuts import render

from rest_framework.permissions import BasePermission

from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User

# Create your views here.


class IsPostRequest(BasePermission):
    def has_permission(self, request, view):
        return request.method == "POST"


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsPostRequest]
