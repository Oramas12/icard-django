from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryApiViewSet  # Asegúrate de que la vista existe

router_category = DefaultRouter()
router_category.register(
    prefix="categories", basename="categories", viewset=CategoryApiViewSet
)

urlpatterns = [
    path("", include(router_category.urls)),  # Asegúrate de que esta línea existe
]
