"""icard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import router_user
from categories.api.router import router_category
from products.api.router import router_product
from tables.api.router import router_table
from orders.api.router import router_orders
from payments.api.router import router_payments
from django.http import JsonResponse

# Configuración de documentación de la API
schema_view = get_schema_view(
    openapi.Info(
        title="iCard - ApiDoc",
        default_version="v1",
        description="Documentación de la API de iCard",
        terms_of_service="https://www.tincode.es/",
        contact=openapi.Contact(email="xagustin93@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

# Página principal
def home(request):
    return JsonResponse({"message": "Welcome to iCard Django API!"})

urlpatterns = [
    path("", home),  # Página de inicio en "/"
    path("admin/", admin.site.urls),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redocs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    
    # Aquí incluimos cada router con su prefijo correcto
    path("api/users/", include("users.api.router")),
    path("api/categories/", include("categories.api.router")),
    path("api/products/", include("products.api.router")),
    path("api/tables/", include("tables.api.router")),
    path("api/orders/", include("orders.api.router")),
    path("api/payments/", include("payments.api.router")),
]

