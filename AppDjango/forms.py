from django import forms


class PeliFormu(forms.Form):
    titulo=forms.CharField(max_length=60)
    director=forms.CharField(max_length=60)
    estreno=forms.DateField()
    duracion=forms.IntegerField()
    genero=forms.CharField(max_length=30)


class ActoFormu(forms.Form):
    nombre=forms.CharField(max_length=60)
    nacimiento=forms.DateField()
    sexo=forms.CharField(max_length=10)
    nacionalidad=forms.CharField(max_length=30)
    participo=forms.IntegerField()


class SeriesFormu(forms.Form):
    titulo=forms.CharField(max_length=60)
    director=forms.CharField(max_length=60)
    temporadas=forms.IntegerField()
    episodios=forms.IntegerField()
    emision=forms.DateField()
    continuidad=forms.BooleanField()