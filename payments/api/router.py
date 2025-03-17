from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryApiViewSet  # Cambia esto según el módulo

router_category = DefaultRouter()
router_category.register(
    prefix='categories', basename='categories', viewset=CategoryApiViewSet
)

urlpatterns = [
    path('', include(router_category.urls)),  # Agregar esto
]
