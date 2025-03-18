from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

def generate_password(request):
    hashed_password = make_password('Admin123!')
    return JsonResponse({'hashed_password': hashed_password})
