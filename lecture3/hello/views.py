from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello vía HttpResponse puesto en la función index en views.py de la app hello")

def saludar(request, nombre):
   #  return HttpResponse(f"<H2>Hola {nombre}</H2>")
    nombre=nombre.capitalize()
    return render(request, "hello/saludar.html", {
       "nombreEnPlantilla": nombre
    } )
def saludarNombreEdad(request, nombre, edad):
    return HttpResponse(f"Hola {nombre}, veo que tienes {edad} años.")

