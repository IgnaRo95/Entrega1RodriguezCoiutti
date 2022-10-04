from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppDjango.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def padre(request):
    return render(request, 'AppCoder/padre.html')

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def sobreNosotros(request):
    return render(request, "AppCoder/sobreNosotros.html")

#--------------------------------------------------------------------------------------------------------------------------------------------------#
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

def busquedaPeli(request):
    return render(request, 'AppCoder/busquedaPeli.html')

def buscarPeli(request):
    if request.GET["titulo"]:
        titulo=request.GET["titulo"]
        peli=Peliculas.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppCoder/resultBusquePeli.html', {"pelicula":peli})
    else:
        return render(request, 'AppCoder/busquedaPeli.html', {"mensaje":"ingrese pelicula"})

def infoPeli(request):
    peliculas=Peliculas.objects.all()
    print(list(peliculas))
    return render(request, 'AppCoder/infoPeli.html', {"peliculas":peliculas})

def editarPelicula(request, id):
    pelicula=Peliculas.objects.get(id=id)
    if request.method=="POST":
        form=PeliFormu(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            pelicula.titulo=info["titulo"]
            pelicula.director=info["director"]
            pelicula.estreno=info["estreno"]
            pelicula.duracion=info["duracion"]
            pelicula.genero=info["genero"]
            pelicula.save()
            peliculas=Peliculas.objects.all
            return render(request, "AppCoder/infoPeli.html", {"peliculas":peliculas})
    else:
        form=PeliFormu(initial={"titulo":pelicula.titulo, "director":pelicula.director,"estreno":pelicula.estreno, "duracion":pelicula.duracion, "genero":pelicula.genero})
        return render(request, 'AppCoder/editarPelicula.html', {"formulario":form, "pelicula":pelicula})

def eliminarPelicula(request, id):
    pelicula=Peliculas.objects.get(id=id)
    pelicula.delete()
    peliculas=Peliculas.objects.all()
    return render(request, 'AppCoder/infoPeli.html', {"peliculas":peliculas})


#------------------------------------------------------------------------------------------------------------------------------------------------#
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

def busquedaActor(request):
    return render(request, 'AppCoder/busquedaAct.html')

def buscarActor(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        nom=Actores.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppCoder/resultBusqueAct.html', {"actor":nom})
    else:
        return render(request, 'AppCoder/busquedaAct.html', {"mensaje":"ingrese actor/actriz"})

def infoActor(request):
    actores=Actores.objects.all()
    print(list(actores))
    return render(request, 'AppCoder/infoActor.html', {"actores":actores})

def editarActor(request, id):
    actor=Actores.objects.get(id=id)
    if request.method=="POST":
        form=ActoFormu(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            actor.nombre=info["nombre"]
            actor.nacimiento=info["nacimiento"]
            actor.sexo=info["sexo"]
            actor.nacionalidad=info["nacionalidad"]
            actor.participo=info["participo"]
            actor.save()
            actores=Actores.objects.all
            return render(request, "AppCoder/infoActor.html", {"actores":actores})
    else:
        form=ActoFormu(initial={"nombre":actor.nombre, "nacimiento":actor.nacimiento,"sexo":actor.sexo, "nacionalidad":actor.nacionalidad, "participo":actor.participo})
        return render(request, 'AppCoder/editarActor.html', {"formulario":form, "actor":actor})

def eliminarActor(request, id):
    actor=Actores.objects.get(id=id)
    actor.delete()
    actores=Actores.objects.all()
    return render(request, 'AppCoder/infoActor.html', {"actores":actores})


#-----------------------------------------------------------------------------------------------------------------------------------------------------#
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

def infoSeries(request):
    series=Series.objects.all()
    print(list(series))
    return render(request, 'AppCoder/infoSeries.html', {"series":series})

def editarSeries(request, id):
    serie=Series.objects.get(id=id)
    if request.method=="POST":
        form=SeriesFormu(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            serie.titulo=info["titulo"]
            serie.director=info["director"]
            serie.temporadas=info["temporadas"]
            serie.episodios=info["episodios"]
            serie.emision=info["emision"]
            serie.continuidad=info["continuidad"]
            serie.save()
            series=Series.objects.all
            return render(request, "AppCoder/infoSeries.html", {"series":series})
    else:
        form=SeriesFormu(initial={"titulo":serie.titulo, "director":serie.director,"temporadas":serie.temporadas, "episodios":serie.episodios, "emision":serie.emision, "continuidad":serie.continuidad})
        return render(request, 'AppCoder/editarSeries.html', {"formulario":form, "serie":serie})

def eliminarSeries(request, id):
    serie=Series.objects.get(id=id)
    serie.delete()
    series=Series.objects.all()
    return render(request, 'AppCoder/infoSeries.html', {"series":series})

def busquedaSeries(request):
    return render(request, 'AppCoder/busquedaSeries.html')

def buscarSeries(request):
    if request.GET["titulo"]:
        titulo=request.GET["titulo"]
        tilt=Series.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppCoder/resultBusqueSeries.html', {"serie":tilt})
    else:
        return render(request, 'AppCoder/busquedaSeries.html', {"mensaje":"ingrese serie"})

#------------------------------------------------------------------------------------------------------------------------------------------------#
#loguear y registrar
def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppCoder/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request, 'AppCoder/login.html', {"formulario":form, "mensaje":"usuario o contraseña incorrectos"})
        else:
            return render(request, 'AppCoder/login.html', {"formulario":form, "mensaje":"usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, 'AppCoder/login.html', {"formulario":form})


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':f'usuario {username} creado correctamente'})
        else:
            return render(request, 'AppCoder/register.html', {'formulario':form, 'mensaje':'FORMULARIO INVALIDADO'})
    else:
        form=UserRegisterForm()
        return render(request, 'AppCoder/register.html', {'formulario':form})

#------------------------------------------------------------------------------------------------------------------------------------------------#
def agregarAvatar(request):
    if request.method == "POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppCoder/inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', 'imagen':avatar.imagen.url, 'avatar':obtenerAvatar(request)})
        else:
            return render(request, 'AppCoder/agregarAvatar.html', {"formulario":formulario, "mensaje":'formulario invalidado', 'avatar':obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
        return render(request, 'AppCoder/agregarAvatar.html', {"formulario":formulario, "usuario":request.user})


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen='/media/avatares/AvatarXdefecto.png'
    return imagen