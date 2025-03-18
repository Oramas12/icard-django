from django.urls import path
from .views import generate_password

urlpatterns = [
    path('generate-password/', generate_password),  # Nueva ruta para generar la contraseña
]
