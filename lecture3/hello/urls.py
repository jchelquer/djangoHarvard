from django.urls import path
from  . import views                # importa views.py donde está definido index()
urlpatterns=[
    path ("", views.index, name="ruta_index"),
    path("<str:nombre>-<int:edad>", views.saludarNombreEdad, name="ruta_stringGuionInt"),
    path("<str:nombre>", views.saludar, name="ruta_saludar")

]