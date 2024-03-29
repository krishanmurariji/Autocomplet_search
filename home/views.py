from django.shortcuts import render
from .models import Names
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def get_names(request):
    payload = []
    search = request.GET.get('search', '')  # Initialize search with an empty string
    if search:  # Check if search is not an empty string
        objs = Names.objects.filter(name__startswith=search)
        for obj in objs:
            payload.append({'name': obj.name})
    return JsonResponse({'status': True, 'payload': payload})