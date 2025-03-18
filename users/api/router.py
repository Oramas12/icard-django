from django.urls import path
from .views import generate_password

urlpatterns = [
    path('users/generate-password/', generate_password, name='generate-password'),
]
