from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    #pelicula
    path('peliculas/', peliculas, name='peliculas'),
    path('busquedaPeli/', busquedaPeli, name='busquedaPeli'),
    path('buscarPeli/', buscarPeli, name='buscarPeli'),
    path('eliminarPelicula/<id>', eliminarPelicula, name='eliminarPelicula'),
    path('editarPelicula/<id>', editarPelicula, name='editarPelicula'),
    path('infoPeli/', infoPeli, name='infoPeli'),
    #actor
    path('actores/', actores, name='actores'),
    path('busquedaActor/', busquedaActor, name='busquedaActor'),
    path('buscarActor/', buscarActor, name='buscarActor'),
    path('eliminarActor/<id>', eliminarActor, name='eliminarActor'),
    path('editarActor/<id>', editarActor, name='editarActor'),
    path('infoActor', infoActor, name='infoActor'),
    #series
    path('series/', series, name='series'),
    path('busquedaSeries/', busquedaSeries, name='busquedaSeries'),
    path('buscarSeries/', buscarSeries, name='buscarSeries'),
    path('eliminarSeries/<id>', eliminarSeries, name='eliminarSeries'),
    path('editarSeries/<id>', editarSeries, name='editarSeries'),
    path('infoSeries', infoSeries, name='infoSeries'),
    #otros
    path('sobreNosotros/', sobreNosotros, name='sobreNosotros'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    #login/registro
    path('login/', login_request, name='login'),
    path('registro/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout')
]
