from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.views import ProductApiViewSet  # Asegúrate de que la vista existe

router_product = DefaultRouter()
router_product.register(
    prefix='products', basename='products', viewset=ProductApiViewSet
)

urlpatterns = [
    path('', include(router_product.urls)),
]
