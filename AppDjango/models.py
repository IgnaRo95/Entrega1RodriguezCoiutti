from django.db import models

# Create your models here.
class Peliculas(models.Model):
    titulo=models.CharField(max_length=60)
    director=models.CharField(max_length=60)
    estreno=models.DateField()
    duracion=models.IntegerField()
    genero=models.CharField(max_length=30)
    def __str__(self):
        return self.titulo


class Actores(models.Model):
    nombre=models.CharField(max_length=60)
    nacimiento=models.DateField()
    sexo=models.CharField(max_length=10)
    nacionalidad=models.CharField(max_length=30)
    participo=models.IntegerField()
    def __str__(self):
        return self.nombre


class Series(models.Model):
    titulo=models.CharField(max_length=60)
    director=models.CharField(max_length=60)
    temporadas=models.IntegerField()
    episodios=models.IntegerField()
    emision=models.DateField()
    continuidad=models.CharField(max_length=10)
    def __str__(self):
        return self.titulo