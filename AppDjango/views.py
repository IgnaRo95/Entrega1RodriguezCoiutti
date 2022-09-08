from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppDjango.forms import *
# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def peliculas(request):
    if request.method == "POST":
        form=PeliFormu(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            director=informacion["director"]
            estreno=informacion["estreno"]
            duracion=informacion["duracion"]
            genero=informacion["genero"]
            peli=Peliculas(titulo=titulo, director=director, estreno=estreno, duracion=duracion, genero=genero)
            peli.save()
            return render(request, 'AppCoder/inicio.html', {"mensaje":"Datos de peli creada!"})
    else:
        formulario=PeliFormu
        return render(request, 'AppCoder/peliculas.html', {"formulario":formulario})


def actores(request):
    if request.method == "POST":
        form=ActoFormu(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            nacimiento=info["nacimiento"]
            sexo=info["sexo"]
            nacionalidad=info["nacionalidad"]
            participo=info["participo"]
            reparto=Actores(nombre=nombre, nacimiento=nacimiento, sexo=sexo, nacionalidad=nacionalidad, participo=participo)
            reparto.save()
            return render(request, 'AppCoder/inicio.html', {"mensaje":"Datos de actores creados!"})
    else:
        formulario=ActoFormu
        return render(request, 'AppCoder/actores.html', {"formulario":formulario})


def series(request):
    if request.method == "POST":
        form=SeriesFormu(request.POST)
        if form.is_valid():
            information=form.cleaned_data
            titulo=information["titulo"]
            director=information["director"]
            temporadas=information["temporadas"]
            episodios=information["episodios"]
            emision=information["emision"]
            continuidad=information["continuidad"]
            serie=Series(titulo=titulo, director=director, temporadas=temporadas, episodios=episodios, emision=emision, continuidad=continuidad)
            serie.save()
            return render(request, 'AppCoder/inicio.html', {"mensaje":"Datos de series creadas!"})
    else:
        formulario=SeriesFormu
        return render(request, 'AppCoder/series.html', {"formulario":formulario})

def busquedaP(request):
    return render(request, 'AppCoder/busquedaPeli.html')

def buscarP(request):
    if request.GET["titulo"]:
        titulo=request.GET["titulo"]
        peli=Peliculas.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppCoder/resultBusquePeli.html', {"pelicula":peli})
    else:
        return render(request, 'AppCoder/busquedaPeli.html', {"mensaje":"ingrese pelicula"})


def busquedaA(request):
    return render(request, 'AppCoder/busquedaAct.html')

def buscarA(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nom=Actores.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppCoder/resultBusqueAct.html', {"actor":nom})
    else:
        return render(request, 'AppCoder/busquedaAct.html', {"mensaje":"ingrese actor/actriz"})


def busquedaS(request):
    return render(request, 'AppCoder/busquedaSeries.html')

def buscarS(request):
    if request.GET["titulo"]:
        titulo=request.GET["titulo"]
        tilt=Series.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppCoder/resultBusqueSeries.html', {"serie":tilt})
    else:
        return render(request, 'AppCoder/busquedaSeries.html', {"mensaje":"ingrese serie"})