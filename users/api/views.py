from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def generate_password(request):
    hashed_password = make_password('Admin123!')
    return JsonResponse({'hashed_password': hashed_password})
