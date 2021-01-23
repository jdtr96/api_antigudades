from django.urls import path, include
from .views import ProductoViewsets, ValoracionViewsets, AceptarVal, ValPro, ProValPro
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'pro', ProductoViewsets, basename="producto")
router.register(r'val', ValoracionViewsets, basename="valoracion")


urlpatterns = [
    path('', include(router.urls)),
    path('aceptar/<int:pk>/', AceptarVal.as_view(), name="aceptar"),
    path('reporte_total/', ValPro.as_view(), name="reporte_total"),
    path('reporte_promedio/', ProValPro.as_view(), name="reporte_promedio"),

]
