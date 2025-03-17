from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.api.views import OrderApiViewSet  # Asegúrate de que esta vista existe

router_orders = DefaultRouter()
router_orders.register(
    prefix='orders', basename='orders', viewset=OrderApiViewSet
)

urlpatterns = [
    path('', include(router_orders.urls)),
]
