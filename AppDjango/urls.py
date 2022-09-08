from django.urls import path
from .views import *

urlpatterns = [
    path('peliculas/', peliculas, name='peliculas'),
    path('inicio/', inicio, name='inicio'),
    path('actores/', actores, name='actores'),
    path('series/', series, name='series'),
    path('busquedaP/', busquedaP, name='busquedaP'),
    path('buscarP/', buscarP, name='buscarP'),
    path('busquedaA/', busquedaA, name='busquedaA'),
    path('buscarA/', buscarA, name='buscarA'),
    path('busquedaS/', busquedaS, name='busquedaS'),
    path('buscarS/', buscarS, name='buscarS'),
    
]
