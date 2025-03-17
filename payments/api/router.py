from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.api.views import PaymentApiViewSet  # Asegúrate de que esta vista existe

router_payments = DefaultRouter()
router_payments.register(
    prefix='payments', basename='payments', viewset=PaymentApiViewSet
)

urlpatterns = [
    path('', include(router_payments.urls)),
]
