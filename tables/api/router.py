from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tables.api.views import TableApiViewSet  # Asegúrate de que esta vista existe

router_table = DefaultRouter()
router_table.register(
    prefix='tables', basename='tables', viewset=TableApiViewSet
)

urlpatterns = [
    path('', include(router_table.urls)),
]
