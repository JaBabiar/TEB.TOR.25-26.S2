from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Verse


def index(request):
    wersy = Verse.objects.all()
    data = []
    for wers in wersy:
        dane = {"Autor": wers.author, "Tekst": wers.verse}
        data.append(dane)
        
    return JsonResponse({"wersy": data})

def mango(request, skibidi):
    wers = Verse.objects.get(id=skibidi)
    data = {"wersy": [{"Autor": wers.author, "Tekst": wers.verse}]}
    return JsonResponse(data)
